import streamlit as st;
import Controllers.ShowController as ShowController;

import pages.show.newShow as newShow;
import pages.show.viewShow as viewShow;
import pages.teatro.newTeatro as newTeatro;
import pages.teatro.viewTeatro as viewTeatro;
import pages.sessao.newSessao as newSessao;


st.sidebar.title('menu')
page = st.sidebar.selectbox('',['home','sessões','nova sessão','compras','comprar ingresso','shows','novo show','teatros','novo teatro'])

if page == 'home' :
    st.title('SITB-sistema de ingressos teatrais de belém')
elif page == 'sessões' :
    st.title('sessões')
elif page == 'nova sessão' :
    st.title('nova sessão')
    newSessao.NewSessao()

elif page == 'compras' :
    st.title('compras')
elif page == 'comprar ingresso' :
    st.title('comprar ingresso')


elif page == 'shows' :

    viewShow.ViewShow()

#novo show
elif page == 'novo show' :
    newShow.NewShow()

elif page == 'teatros' :
    viewTeatro.ViewTeatro()

elif page == 'novo teatro':
    newTeatro.NewTeatro()