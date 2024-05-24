import streamlit as st

def cadastro():
    contador = 0
    while contador < 3:
        nome = st.text_input("Digite o nome para o cadastro: ", key=f"nome{contador}")
        senha = st.text_input("Digite uam senha para o cadastro:", type="password", key=f"senha{contador}")
        csenha = st.text_input("Confirme a senha:", type="password", key=f"csenha{contador}")

    if st.button("Cadastrar",key=f"Cadastrar{contador}"):
        if senha == csenha:
            st.success(f"Seja bem vindo: {nome}")

