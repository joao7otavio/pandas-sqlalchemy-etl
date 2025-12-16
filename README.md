# 📊 Sistema de Monitoramento de TI (ETL + Dashboard)

Este projeto é uma solução completa de **Business Intelligence (BI)** e Engenharia de Dados. Ele simula o dia a dia de uma área de TI, onde dados brutos de chamados são extraídos, transformados via Python e apresentados em um Dashboard interativo para tomada de decisão.

O projeto demonstra o ciclo completo do dado (**Full Stack Data**):
1.  **Ingestão e Tratamento (ETL)** com Pandas.
2.  **Armazenamento** em Banco de Dados SQL.
3.  **Visualização** com Streamlit.

---

## 🎯 Funcionalidades

### 1. ⚙️ Automação de Dados (Back-end)
O script `main.py` executa o pipeline ETL:
* **Extração:** Lê o arquivo bruto `chamados.csv`.
* **Transformação:**
    * Limpa dados inconsistentes e padroniza textos.
    * Filtra apenas chamados finalizados ("Fechado").
    * **Rastreabilidade:** Adiciona a assinatura `Script_JoaoOtavio` para auditar quem processou o dado no banco.
* **Carga:** Salva os dados tratados automaticamente no MySQL (tabela `relatorio_chamados`).

### 2. 📈 Dashboard Gerencial (Front-end)
O painel `dashboard.py` conecta no banco e exibe em tempo real:
* **KPIs:** Total de chamados, demandas exclusivas de TI e volume de automação.
* **Gráficos:** Análise por Departamento (Setor) e Status dos chamados.
* **Dados Detalhados:** Visualização tabular completa dos registros filtrados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Pandas:** Manipulação e limpeza de dados (ETL).
* **Streamlit:** Criação do Dashboard interativo Web.
* **SQLAlchemy & PyMySQL:** Conexão e ORM com Banco de Dados.
* **Python-Dotenv:** Segurança de credenciais e variáveis de ambiente.
* **MySQL:** Banco de dados relacional.

---

## 📂 Estrutura do Projeto

* `main.py`: Script responsável pelo ETL (deve ser rodado primeiro).
* `dashboard.py`: Aplicação Web do Dashboard (visualização).
* `chamados.csv`: Base de dados de exemplo (input).
* `.env.example`: Modelo de configuração das credenciais (segurança).
* `requirements.txt`: Lista de todas as bibliotecas necessárias.

---

## 🚀 Como Executar o Projeto

### 1. Preparação
Clone o repositório e instale as dependências listadas:

```
pip install -r requirements.txt
```

### 2. Configuração do Banco de Dados
Certifique-se de ter um banco MySQL criado com o nome `gestao_ti`. 
Na raiz do projeto, duplique o arquivo `.env.example` e renomeie para `.env`. Abra o arquivo `.env` e coloque a sua senha do banco:

```
DB_USER=root
DB_PASS=sua_senha_real_aqui
DB_HOST=localhost
DB_NAME=gestao_ti
```

### 3. Rodando a Automação (ETL)
Execute o script para processar o CSV e alimentar o banco de dados:

```
python main.py
```
Você verá a mensagem: "Processo ETL concluído com sucesso!"

### 4. Abrindo o Dashboard
Inicie o servidor do Streamlit para visualizar os gráficos:

```
streamlit run dashboard.py
```
O painel abrirá automaticamente no seu navegador.