import streamlit as st;
import Controllers.ShowController as ShowController;
import models.Show as Show;
import pandas as pd;


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
    for item in ShowController.selecionarTodos():
        costumerList.append([item.name, item.location, item.description])

    df = pd.DataFrame(
        costumerList,
        columns=['id','nome','descrição']
    )

    st.table(df)

#novo show
elif page == 'novo show' :
    st.title('novo show')

    with st.form(key="new_show"):

        showname = st.text_input(label='insira o nome')
        showdescription = st.text_area(label='descrição')
        teste = st.selectbox('',ShowController.selecionarName())

        input_button_submit = st.form_submit_button('cadastar novo show')

    if input_button_submit:

        show_id = ShowController.idShow()
        show_name = showname
        show_description = showdescription

        ShowController.incluir(show_id, show_name, show_description)
        st.success('show cadastrado com sucesso')