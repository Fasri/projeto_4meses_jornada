import streamlit as st
import pandas as pd

# Título do app
st.title("📊 Planner Interativo - Jornada de Dados")

# Upload do arquivo
uploaded_file = st.file_uploader("📁 Faça upload da planilha (xlsx):", type=["xlsx"])

if uploaded_file:
    # Listar as abas
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names
    aba = st.selectbox("📅 Selecione a semana:", sheet_names)

    # Carregar a aba selecionada
    df = pd.read_excel(uploaded_file, sheet_name=aba)

    # Mostrar a tabela editável
    st.write("✍️ Edite abaixo seu progresso:")
    edited_df = st.data_editor(
        df,
        num_rows="dynamic",
        use_container_width=True,
        key=aba
    )

    # Botão para download
    st.markdown("---")
    st.download_button(
        label="⬇️ Baixar planilha atualizada",
        data=edited_df.to_excel(index=False, engine='openpyxl'),
        file_name=f"{aba}_Planner_Editado.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
