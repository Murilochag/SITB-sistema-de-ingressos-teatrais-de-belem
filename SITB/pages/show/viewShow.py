
from turtle import onclick
import streamlit as st;
import Controllers.ShowController as ShowController;

def ViewShow():
    coluns = st.columns((1,2,2))
    campos = ['id', 'nome', 'descrição','excluir']
    for col, campo_nome in zip(coluns, campos):
        col.write(campo_nome)
    
    for item in ShowController.selecionarTodos():
        col1, col2, col3, col4 = st.columns((1,2,4,1))
        col1.write(item.id)
        col2.write(item.name)
        col3.write(item.description)
        button_space = col4.empty()
        on_click_Excluir = button_space.button('Excluir', 'btnExcluir' + str(item.id))

        if on_click_Excluir:
            ShowController.ExcluirShow(item.id)