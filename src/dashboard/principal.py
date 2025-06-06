import streamlit as st

from src.dashboard.chat.conversa_chat import get_conversa


def _principal():

    get_conversa()

def get_principal_page() -> st.Page:
    """
    Função para retornar a página principal.
    :return: st.Page - A página principal do aplicativo.
    """
    return st.Page(
        _principal,
        title="Principal",
        url_path="/"
    )