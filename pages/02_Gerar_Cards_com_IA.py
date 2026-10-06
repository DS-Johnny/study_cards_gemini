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

        st.session_state["dados"] = json.loads(resultado.text)


    except Exception as e:
        st.session_state["dados"] = None
        st.warning(resultado)


# ============================================================
# EXIBIR Perguntas
# ============================================================

try:
    if st.session_state["dados"]:

        # st.write(st.session_state["dados"])
        for i,kv in enumerate(st.session_state["dados"].items()):
            st.markdown(f"# Pergunta {i+1}")
            st.markdown(f"### {kv[0]}")
            st.markdown(f'- Resposta: {kv[1]}')
            st.markdown('---')


        # ========================================================
        # DOWNLOAD
        # ========================================================

        with st.popover("Salvar Arquivo"):

            nome_arquivo = st.text_input(
                "Nome do Arquivo"
            )
            st.write(f'{nome_arquivo}.json')
            st.download_button(
                label="Download",

                data=json.dumps(
                    st.session_state["dados"],
                    indent=4,
                    ensure_ascii=False
                ),

                file_name=f"{nome_arquivo}.json",

                mime="application/json",

                icon=":material/download:",

                width=600
            )
except:
    pass