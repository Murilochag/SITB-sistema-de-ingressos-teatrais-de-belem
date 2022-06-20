import streamlit as st;
import Controllers.ShowController as ShowController;

import pages.show.newShow as newShow;
import pages.show.viewShow as viewShow;
import pages.teatro.newTeatro as newTeatro;
import pages.teatro.viewTeatro as viewTeatro;


st.sidebar.title('menu')
page = st.sidebar.selectbox('',['home','sessões','nova sessão','compras','comprar ingresso','shows','novo show','teatros','novo teatro'])

if page == 'home' :
    st.title('SITB-sistema de ingressos teatrais de belém')
elif page == 'sessões' :
    st.title('sessões')
elif page == 'nova sessão' :
    st.title('nova sessão')


    with st.form(key="new_sessao"):

        showname = st.text_input(label='insira o nome')
        showdescription = st.text_area(label='descrição')
        teste = st.selectbox('',ShowController.selecionarName())

        input_button_submit = st.form_submit_button('cadastar novo show')

elif page == 'compras' :
    st.title('compras')
elif page == 'comprar ingresso' :
    st.title('comprar ingresso')


elif page == 'shows' :
    st.title('shows')

    viewShow.ViewShow()

#novo show
elif page == 'novo show' :
    newShow.NewShow()

elif page == 'teatros' :
    viewTeatro.ViewShow()

elif page == 'novo teatro':
    newTeatro.NewTeatro()