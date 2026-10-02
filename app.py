import streamlit as st
# from gerador import Gerador
import json
from random import choice

with open('log_perguntas.json', 'r' , encoding='utf-8') as f:
    logs = json.load(f)

# cards = Gerador("gemini-3.5-flash")


cards = json.loads(logs[0]['Resposta']['candidates'][0]['content']['parts'][0]['text'])


pergunta = choice([pergunta for pergunta in cards.keys()])
resposta = cards[pergunta]

# p, r = st.tabs(['Pergunta', 'Resposta'])

# with p:
#     st.title(pergunta)
# with r:
#     st.title(resposta)
    
# if st.button('Recarregar'):
#     st.reload()

with open('style.txt', 'r', encoding='utf-8') as f:
    estilo = f.read()

st.markdown(estilo, unsafe_allow_html=True)

st.html(f"""<div class="card">
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
</div>""")


if st.button('Próxima Pergunta', width=900):
    st.rerun()


with st.popover("Salvar Arquivo"):
    
    file_name = st.text_input("Nome do Arquivo",'cards')
    st.download_button(
        label="Download",
        data=json.dumps(cards,
                        indent=4,
                        ensure_ascii=False  ),
        file_name=f"{file_name}.json",
        mime="application/json",
        icon=":material/download:",
        width=600
    )


    
