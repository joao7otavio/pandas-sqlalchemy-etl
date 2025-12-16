import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Painel de Chamados", page_icon="💻", layout="wide")

load_dotenv()

@st.cache_data
def carregar_dados():
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    string_conexao = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"

    engine = create_engine(string_conexao)
    query = "SELECT * FROM relatorio_chamados"

    df = pd.read_sql(query, engine)
    return df

st.title("💻 Painel de Controle - Suporte TI")
st.write("Visão geral dos atendimentos finalizados no mês.")
st.markdown("---")

try:
    df = carregar_dados()

    col1, col2, col3 = st.columns(3)

    total = len(df)
    chamados_ti = len(df[df['area'] == 'TI'])
    processados_auto = len(df[df['processado_por'] == 'Script_JoaoOtavio'])

    col1.metric("Chamados Fechados", total)
    col2.metric("Chamados só da TI", chamados_ti)
    col3.metric("Processados pelo Script", processados_auto)

    st.markdown("---")

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.subheader("Chamados por Setor")
        st.caption("Qual área pediu mais ajuda?")
        contagem_area = df['area'].value_counts()
        st.bar_chart(contagem_area)

    with col_graf2:
        st.subheader("Situação Atual")
        st.caption("Tudo o que foi filtrado pelo robô")
        contagem_status = df['status'].value_counts()
        st.bar_chart(contagem_status, color="#ffaa00")

    st.markdown("---")
    st.subheader("Lista Completa")

    with st.expander("Ver todos os dados"):
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("❌ Erro ao conectar no banco")
    st.warning("Confere se o MySQL está rodando aí.")
    st.code(f"Erro técnico: {e}")