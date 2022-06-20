from unicodedata import name
import streamlit as st;
import Controllers.TeatroController as TeatroController;

def NewTeatro():
    st.title('novo teatro')

    with st.form(key="new_teatro"):

        nome = st.text_input(label='insira o nome:')
        capacidade = st.number_input("insira a capadidade do teatro:", 1,5000)

        input_button_submit = st.form_submit_button('cadastar novo show')

    if input_button_submit: 
        id_teatro = TeatroController.idTeatro()
        name_teatro = nome
        capacidade_teatro = capacidade

        TeatroController.incluir(id_teatro, name_teatro, capacidade_teatro)
        st.success('teatro cadastrado com sucesso')