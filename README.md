# Automação de Relatório de TI com Python (ETL)

Este projeto é um script de automação ETL (Extract, Transform, Load) construído em Python. Ele foi desenvolvido como um projeto prático para demonstrar habilidades em lógica de programação, manipulação de dados e integração com bancos de dados.

O script simula um cenário real de TI onde relatórios de chamados (em formato `.csv`) são lidos, processados e carregados em um banco de dados MySQL para análise.

---

## 🎯 O que o projeto faz?

O script executa um processo ETL completo em 4 etapas:

1.  **Extract (Extrair):** Lê um arquivo `chamados.csv` contendo o relatório de chamados de TI.
2.  **Transform (Transformar):** Aplica regras de negócio para limpar e preparar os dados.
    * **Padroniza** a coluna `area` para letras maiúsculas.
    * **Filtra** o relatório, mantendo apenas os chamados com status "Fechado".
    * **Adiciona** uma nova coluna (`processado_por`) para rastrear quais dados foram processados pelo script.
3.  **Load (Carregar):** Conecta-se a um banco de dados MySQL e salva os dados limpos e transformados em uma tabela chamada `relatorio_chamados`. Se a tabela já existir, ela é substituída com os dados mais recentes.

---

## 🛠️ Tecnologias Utilizadas

* **Python3:** Linguagem principal do projeto.
* **Pandas:** Para a leitura (`read_csv`) e toda a manipulação dos dados (filtrar, transformar).
* **SQLAlchemy:** Para criar a "engine" de conexão robusta com o banco de dados.
* **PyMySQL:** Como o "driver" (tradutor) para permitir a comunicação entre o SQLAlchemy e o MySQL.
* **Python-Dotenv:** Para proteger dados sensíveis (como usuário e senha do banco), carregando-os a partir de um arquivo `.env` ignorado pelo Git.

---

## 🚀 Como Executar o Projeto

1.  Clone este repositório.
2.  Certifique-se de ter o Python3 instalado.
3.  Crie um ambiente virtual (`.venv`) e instale as dependências:
    ```bash
    pip install pandas sqlalchemy pymysql python-dotenv
    ```
4.  Crie um banco de dados MySQL chamado `gestao_ti`.
5.  Na raiz do projeto, crie um arquivo `.env` e adicione suas credenciais (este arquivo não é monitorado pelo Git):
    ```text
    DB_USER=seu_usuario_mysql
    DB_PASS=sua_senha_mysql
    DB_HOST=localhost
    DB_NAME=gestao_ti
    ```
6.  Execute o script principal:
    ```bash
    python main.py
    ```
7.  Após a execução, verifique a tabela `relatorio_chamados` no seu banco `gestao_ti`.