import streamlit as st;
import Controllers.SessaoController as SessaoController;
import Controllers.TeatroController as TeatroController;
import Controllers.ShowController as ShowController;

def NewSessao():
    st.title('nova sessão')

    with st.form(key="new_show"):

        teatro = st.selectbox('selecione um teatro',TeatroController.selecionarTeatro())
        show = st.selectbox('selecione um show', ShowController.selecionarShow())
        data = st.date_input('selecione uma data')
        hora = st.time_input('selecione um horário')

        input_button_submit = st.form_submit_button('cadastar nova sessao')

    if input_button_submit:

        sessao_teatro = teatro
        sessao_show = show
        sessao_data = data
        sessao_hora = hora
    

        SessaoController.incluir(SessaoController.idSessao(), sessao_teatro, sessao_show, sessao_data, sessao_hora)
        st.success('sessao cadastrada com sucesso')