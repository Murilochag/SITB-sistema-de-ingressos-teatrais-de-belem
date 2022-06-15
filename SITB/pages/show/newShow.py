import streamlit as st;
import Controllers.ShowController as ShowController;

def NewShow():
    st.title('novo show')

    with st.form(key="new_show"):

        showname = st.text_input(label='insira o nome')
        showdescription = st.text_area(label='descrição')

        input_button_submit = st.form_submit_button('cadastar novo show')

    if input_button_submit:

        show_id = ShowController.idShow()
        show_name = showname
        show_description = showdescription

        ShowController.incluir(show_id, show_name, show_description)
        st.success('show cadastrado com sucesso')