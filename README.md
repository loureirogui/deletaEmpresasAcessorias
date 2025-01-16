# 🛠️ Deletar Empresas em Massa no Sistema Acessórias

Este projeto é uma ferramenta automatizada para deletar empresas em massa no sistema Acessórias. Ele utiliza Selenium para interagir com a interface web do sistema, abrindo uma aba para cada empresa listada em uma planilha Excel (`deletar.xlsx`) e excluindo-a automaticamente.

⚠️ **Atenção:** 
- Este script realiza exclusões permanentes, portanto, utilize-o com cautela.
- Todas as empresas listadas no arquivo `deletar.xlsx` serão removidas definitivamente do sistema.

---

## 🚀 Como usar

1. Gere o **Relatório Excell Compacto** no sistema Acessórias na seção **Empresas**.
2. Renomeie o arquivo gerado para `deletar.xlsx` e coloque-o na mesma pasta deste script.
3. Certifique-se de que todas as dependências estão instaladas.
4. Execute o script e siga as instruções na tela.

### 📝 Pré-requisitos

- Python 3.7+
- Navegador **Microsoft Edge** instalado.
- Conta válida no sistema Acessórias com permissões para deletar empresas.

---

## 🧑‍💻 Instalação

1. Clone este repositório ou baixe os arquivos:
    ```bash
    git clone https://github.com/seuusuario/seuprojeto.git
    cd seuprojeto
    ```

2. Instale as dependências listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. Certifique-se de que o WebDriver do Edge está configurado corretamente:
    - O script utiliza o `webdriver-manager` para gerenciar a versão do WebDriver automaticamente.

---

## ⚙️ Funcionamento do Script

1. O script solicita as credenciais de login no sistema Acessórias.
2. Lê os IDs das empresas da coluna **B** da planilha `deletar.xlsx`.
3. Realiza login no sistema e cria uma aba para cada empresa a ser deletada.
4. Utiliza threads para realizar múltiplas exclusões em paralelo, otimizando o tempo de execução.

---

## 🛡️ Segurança

- Certifique-se de que o arquivo `deletar.xlsx` contém apenas os IDs das empresas que devem ser removidas.
- Verifique a segurança da máquina onde este script será executado, pois ele armazena credenciais temporariamente durante a execução.

---

## 🐛 Erros Comuns

1. **Erro no login:** 
   - Verifique se o email e a senha estão corretos.
   - Confirme que o sistema Acessórias está acessível.

2. **Planilha não encontrada:**
   - Certifique-se de que o arquivo `deletar.xlsx` está na mesma pasta do script.

3. **Timeout ao deletar empresas:**
   - Execute o script novamente para concluir as exclusões pendentes.

---

## 📂 Estrutura de Arquivos

seuprojeto/ │ 
├── deletar_empresas.py # Código principal 
├── deletar.xlsx # Planilha com os IDs das empresas 
├── requirements.txt # Dependências do projeto 
└── README.md
