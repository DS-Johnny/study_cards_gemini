import streamlit as st
from gerador import Gerador
import json
from random import choice


# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================

st.set_page_config(
    page_title="Gerador de Cards",
    page_icon="🧠"
)




gerador = Gerador("gemini-3.5-flash")



# ============================================================
# INTERFACE
# ============================================================

tema = st.text_input("Digite o tema escolhido")


# ============================================================
# GERAR CARDS
# ============================================================

if st.button("Gerar cards") and tema:

    try:

        resultado = gerador.gerar_perguntas(tema)

        cards = json.loads(resultado.text)


    except Exception as e:
        cards = None
        st.warning(resultado)


# ============================================================
# EXIBIR Perguntas
# ============================================================


    if cards:

        st.write(cards)


        # ========================================================
        # DOWNLOAD
        # ========================================================

        with st.popover("Salvar Arquivo"):

            file_name = st.text_input(
                "Nome do Arquivo",
                "cards"
            )

            st.download_button(
                label="Download",

                data=json.dumps(
                    cards,
                    indent=4,
                    ensure_ascii=False
                ),

                file_name=f"{file_name}.json",

                mime="application/json",

                icon=":material/download:",

                width=600
            )