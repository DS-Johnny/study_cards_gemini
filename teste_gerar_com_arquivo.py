import streamlit as st

file = st.file_uploader('Carregue um arquivo.')

st.write(file.type)

if file.type == 'application/pdf':
    st.write('pdf')

elif file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    st.write('docx')

elif file.type == 'text/plain':
    st.write('txt')
    file = open()



st.write(file)