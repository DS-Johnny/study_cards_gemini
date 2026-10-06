import streamlit as st
import json
from random import choice


arquivo = st.file_uploader("Carregue seu arquivo", type=".json")


# =========================
# CARREGAR ARQUIVO
# =========================

if arquivo is not None and st.button("Carregar"):

    cards = json.load(arquivo)

    st.session_state["dados"] = cards
    st.session_state["carregado"] = True

    # Escolhe a primeira pergunta
    st.session_state["pergunta"] = choice(list(cards.keys()))


# =========================
# EXIBIR CARD
# =========================

if st.session_state.get("carregado", False):

    dados = st.session_state["dados"]
    pergunta = st.session_state["pergunta"]
    resposta = dados[pergunta]

    st.success("Arquivo carregado")

    with open("style.txt", "r", encoding="utf-8") as f:
        estilo = f.read()

    st.markdown(estilo, unsafe_allow_html=True)

    st.html(f"""
    <div class="card">
        <div class="upper-part">
            <div class="upper-part-face">{pergunta}</div>
            <div class="upper-part-back">
                {resposta}
            </div>
        </div>

        <div class="lower-part">
            <div class="lower-part-face">Pergunta</div>
            <div class="lower-part-back">Resposta</div>
        </div>
    </div>
    """)


    # =========================
    # NOVA PERGUNTA
    # =========================

    if st.button("Recarregar"):

        st.session_state["pergunta"] = choice(list(dados.keys()))

        st.rerun()

    with st.popover("Salvar Arquivo"):

            nome_arquivo = st.text_input(
                "Nome do Arquivo",
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