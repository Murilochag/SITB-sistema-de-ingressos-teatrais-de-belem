import streamlit as st;
import Controllers.TeatroController as TeatroController;

def ViewShow():
    colms = st.columns((1,1,1,1))
    campos = ['id', 'nome', 'capacidade','']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)
    
    for item in TeatroController.selecionarTodos():
        col1, col2, col3, col4 = st.columns((1,1,1,1))
        col1.write(item.id)
        col2.write(item.name)
        col3.write(item.capacity)
        button_space_excluir = col4.empty()
        on_click_Excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))

        if on_click_Excluir:
            TeatroController.ExcluirTeatro(str(item.id))
            st.success('teatro ' + item.name + ' excluido com cucesso')