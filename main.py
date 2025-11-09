import pandas as pd
import sys
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

arquivo_csv = "chamados.csv"
print(f"Iniciando a leitura do arquivo: {arquivo_csv}")

try:
    df = pd.read_csv(arquivo_csv)
    print("Sucesso! Dados lidos do CSV:")
    print(df)
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_csv}' não encontrado.")
    sys.exit()
except Exception as e:
    print(f"Erro inesperado ao ler o CSV: {e}")
    sys.exit()

print("-" * 75)

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

string_conexao = string_conexao = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"

try:
    engine = create_engine(string_conexao)

    with engine.connect() as conexao:
        print("Sucesso! Conexão com o banco de dados estabelecida.")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    sys.exit()

print("-" * 75)

print("Iniciando transformação e limpeza dos dados...")

df_transformado = df.copy()

try:
    df_transformado['area'] = df_transformado['area'].str.upper()
    print("Regra 1: Coluna 'area' padronizada para maiúsculas.")
except Exception as e:
    print(f"Erro ao transformar a coluna 'area': {e}")
    sys.exit()

try:
    df_final = df_transformado[df_transformado['status'] == 'Fechado'].copy()
    print("Regra 2: Filtrados apenas os chamados com status 'Fechado'.")

    if df_final.empty:
        print("Aviso: Nenhum chamado com status 'Fechado' encontrado. Encerrando o programa.")
        sys.exit()

except Exception as e:
    print(f"Erro ao filtrar por status: {e}")
    sys.exit()

try:
    df_final['processado_por'] = 'Script_do_Joao'
    print("Regra 3: Coluna 'processado_por' adicionada.")
except Exception as e:
    print(f"Erro ao adicionar nova coluna: {e}")
    sys.exit()

print("Sucesso! Dados transformados e prontos para carregar:")
print(df_final)

print("-" * 75)

print("Iniciando carregamento dos dados no banco...")

try:
    df_final.to_sql(
        'relatorio_chamados',
        engine,
        if_exists='replace',
        index=False
    )

    print("Sucesso! Os dados foram salvos na tabela 'relatorio_chamados'!")

except Exception as e:
    print(f"Erro ao salvar os dados no banco: {e}")
    sys.exit()

print("-" * 75)
print("Processo ETL concluído com sucesso!")