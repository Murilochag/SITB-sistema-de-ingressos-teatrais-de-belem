import streamlit as st
import sqlite3
import data.showdb as showdb
import pandas as pd

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
    costumerList = []

    for item in showdb.selecionarTodos():
        costumerList.append(item.id, item.name, item.lacation, item.description)

    df = pd.DataFrame(
        costumerList = ['id','nome','local','descrição']
    )

    st.table(df)

#novo show
elif page == 'novo show' :
    st.title('novo show')

    with st.form(key="new_show"):
        showname = st.text_input(label='insira o nome')
        showlocation = st.selectbox('selecione o teatro',['teatro da paz','estação gasõmestro','waldemar henrique','teatro do sesi','margarida schivasappa'])
        showdescription = st.text_area(label='descrição')

        input_button_submit = st.form_submit_button('cadastar novo show')

    if input_button_submit :
        showid = showdb.idShow()
        showdb.insertInShow(showid,showname,showlocation,showdescription)
        st.success('Show cadastrado com sucesso!')