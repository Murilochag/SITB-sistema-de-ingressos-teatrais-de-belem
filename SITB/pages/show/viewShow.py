
from turtle import onclick
import streamlit as st;
import Controllers.ShowController as ShowController;

def ViewShow():
    colms = st.columns((1,2,4,1))
    campos = ['id', 'nome', 'descrição','excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)
    
    for item in ShowController.selecionarTodos():
        col1, col2, col3, col4 = st.columns((1,2,4,1))
        col1.write(item.id)
        col2.write(item.name)
        col3.write(item.description)
        button_space_excluir = col4.empty()
        on_click_Excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))

        if on_click_Excluir:
            st.write('funcionando')
            st.write('id=' + item.id)
            ShowController.mostrarId(item.id)
            ShowController.ExcluirShow(str(item.id))