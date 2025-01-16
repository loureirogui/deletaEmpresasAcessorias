import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import openpyxl
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from art import text2art, tprint  # Importa as funções da biblioteca art


tprint("Deletar\nEmpresas", font="starwars")

print("Seja bem-vindo à gambiarra desenvolvida para deletar empresas em massa no sistema Acessórias.\n"
      "Para utilizar, gere o relatório Excell Compacto no campo Empresas do Acessórias!\n"
      "Lembre-se! todas as empresas que estiverem na planilha serão removidas definitivamente.\n"
      "Depois é só colocar a planilha na mesma pasta desse código com o nome (deletar.xlsx)\n"
      "Em alguns casos onde existem muitas empresas para deletar pode ser necessário rodar\n"
      "O código mais de uma vez pois são muitas requisições ao mesmo tempo e pode dar timeout.")


perguntaSeguranca = input("Realizou as instruções acima? (Pressione Enter para prosseguir ou Ctrl+C para encerrar a execução do script.\n")

# Solicita e armazena as credenciais do usuário Acessórias
emailLogin = input("Qual seu email de login no Acessórias?\n")
senhaLogin = input("Qual sua senha de login no Acessórias?\n")


print("\nIniciando o processo de exclusão das empresas\n"
      "Uma janela do Edge será aberta com uma guia para cada empresa"
      "Basta minimizar e aguardar a conclusão do processo")



# Configura as opções do Selenium Webdriver
edge_options = Options()
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
edge_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

# Abre o link de login desejado
url = f"https://app.acessorias.com/"
edge_driver.get(url)


workbook = openpyxl.load_workbook('deletar.xlsx') # Carrega a planilha com nome deletar.xlsx
sheet = workbook.active # Seleciona a planilha ativa 
coluna = 'B' # Seleciona a coluna com os IDS do cliente

# Lógica de login no sistema Acessórias
try:
    email_input = WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'mailAC'))
    )
    email_input.send_keys(emailLogin)
    
    senha_input = WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'passAC'))
    )
    senha_input.send_keys(senhaLogin)
    
    login_button = WebDriverWait(edge_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.rounded.large.expanded.primary-degrade.btn-enviar'))
    )
    login_button.click()

except Exception as e:
    print(f"Erro ao realizar o login, por favor, tente novamente.")

time.sleep(2) # Espera 2 segundos após o login para não dar erro de carregamento

def deletar_empresa(idEmpresa): # Função para abrir uma nova aba e carregar a URL de exclusão
    try:
        edge_driver.execute_script(f"window.open('https://app.acessorias.com/cadempresasdelid.php?EmpID={idEmpresa}&PS={senhaLogin}', '_blank');")

        print(f"Empresa de id {idEmpresa} em processo de exclusão.")

        time.sleep(1) # Pequeno delay para evitar sobrecarga
    except Exception as e:
        print(f"Empresa de id {idEmpresa} não foi excluída. Log de erro {str(e)}")

# Loop por cada empresa e usa threads para deletar em paralelo
threads = []
for cell in sheet[coluna][3:]:
    idEmpresa = cell.value
    if idEmpresa:
        thread = threading.Thread(target=deletar_empresa, args=(idEmpresa,))
        threads.append(thread)
        thread.start()

# Espera todas as threads terminarem
for thread in threads:
    thread.join()

print("Processo de exclusão concluído.")
