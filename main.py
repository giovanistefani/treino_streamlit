import streamlit as st
import pandas as pd
from src.schema import ContratoFuncionarios


def validar(csv):
    """
    Validar o csv
    """
    try:
        df = pd.read_csv(csv)
        erros = []

        for idx, row in df.iterrows():
            try:
                ContratoFuncionarios(**row.to_dict())
            except Exception as e:
                erros.append(f"Erro na linha:{idx+2} {e}")

        if erros:
            st.error("Erros encontrados no arquivo enviados:")
            for erro in erros:
                st.error(erro)
            else:
                st.success("Arquivo validado com sucesso!")
                return True

    except:
        st.error(
            "Erro ao ler o arquivo. Verifique se o arquivo foi enviado corretamente."
        )


def main():
    """função principal"""
    st.set_page_config(page_title="Validador de CSV", layout="wide")
    st.title("Validador de CSV")
    st.write("Escolha o arquivo CSV a ser validado")

    csv = st.file_uploader("Escolha o arquivo CSV", type=["csv"])

    botao = st.button("Validar")

    if botao:
        validar(csv)


if __name__ == "__main__":
    main()
