


import streamlit as st



st.title('Sistema de Média de notas')


nome  =  st.text_input('Nome: ')


nota1 =  st.number_input('Nota 1', value = 0.0)
nota2 =  st.number_input('Nota 2', value = 0.0)
nota3 =  st.number_input('Nota 3', value = 0.0)


media  =  (nota1 +  nota2 +  nota3) / 3
st.write(f'Media: aluno {nome}', media)



