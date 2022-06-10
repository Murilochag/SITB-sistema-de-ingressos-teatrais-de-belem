import streamlit as st
import sqlite3
import services.showdb as showdb

##st.title('SITB-sistema de ingressos teatrais de belém')
st.sidebar.title('menu')
page = st.sidebar.selectbox('',['home','sessões','nova sessão','compras','comprar ingresso','shows','novo show'])

if page == 'home' :
    st.title('SITB-sistema de ingressos teatrais de belém')
elif page == 'sessões' :
    st.title('sessões')
elif page == 'nova sessão' :
    st.title('nova sessão')
elif page == 'compras' :
    st.title('compras')
elif page == 'comprar ingresso' :
    st.title('comprar ingresso')
elif page == 'shows' :
    st.title('shows')
#novo show
elif page == 'novo show' :
    st.title('novo show')

    with st.form(key="new_show"):
        showid = st.text_input(label='insira o id')
        showname = st.text_input(label='insira o nome')
        showlocation = st.selectbox('selecione o teatro',['teatro da paz','margarida saquivasapa e tal','teatro do sesi'])
        input_button_submit = st.form_submit_button('cadastar novo show')

    if input_button_submit :
        showdb.insertInShow(showid,showname,showlocation)