import streamlit as st

# Definir funções
def cadastro():
    nome = st.text_input("Digite o nome para o cadastro:", key="nome")
    senha = st.text_input("Digite uma senha para o cadastro:", type="password", key="senha")
    csenha = st.text_input("Confirme a senha:", type="password", key="csenha")

    if st.button("Cadastrar"):
        if senha == csenha:
            st.success(f"Seja Bem-Vindo: {nome}")
        else:
            st.error("Senhas não conferem. Tente novamente.")

def informacoes_cliente():
    nome = st.text_input("Digite seu nome:")
    idade = st.number_input("Digite sua idade:", min_value=0, step=1)
    peso = st.number_input("Digite seu peso:", min_value=0.0, format="%.2f")
    altura = st.number_input("Digite sua altura:", min_value=0.0, format="%.2f")

    if st.button("Enviar Informações"):
        st.write("-------------------------------")
        st.write(f"Esse é seu nome: {nome}")
        st.write(f"Essa é sua idade: {idade}")
        st.write(f"Esse é seu peso: {peso}")
        st.write(f"Essa é sua altura: {altura}")

def tabela_imc():
    st.write("----Classificação IMC----")
    st.write("----IMC-----|-----Classificação----")
    st.write("Menor que 18.5 | Abaixo do peso")
    st.write("18.5 - 24.9 | Peso normal")
    st.write("25 - 29.9 | Sobrepeso")
    st.write("30 - 34.9 | Obesidade Grau I")
    st.write("35 - 39.9 | Obesidade Grau II")
    st.write("Maior que 40 | Obesidade Grau III")

def calcular_imc(peso, altura):
    if altura > 0:
        imc = peso / (altura ** 2)
        return imc
    return None

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def exibirtreino(nometreino):
    treinos = {
        "1": ["GRAVITON (N) 4X10", "PUXADOR FRENTE (N) 4X12, 3X8", "PUXADOR INVERSO 4X12, 3X8",
              "REMADA CURVA (PRO) 4X12", "ROSCA INVERSA POLIA 3X15", "ROSCA SCOOT 4X12(FI) 2X8(UNI)",
              "ELEVAÇÃO LATERAL(POLIA) 3X10+FALHA", "HIT + ABS INFRA + AERÓBICO"],
        "2": ["HACK MACHINE 4X10, 12, 2X10", "HAC 45 4X12, 3X10", "AFUNDO 4X10, 1X12, 2X10",
              "CADEIRA FLEXORA + PASSADA 4X12, 15", "CADEIRA EXTENSORA 4XISO5'+15", "PANTURRILHA 3X20"],
        "3": ["MANGUITOS AQUE", "DESENVOLVIMENTO 3X15", "CRUCIFIXO INVERSO 3X15", "ELEV. LAT PO. 5X15",
              "DESENVOLV HALT 3X15", "ADUÇÃO+ABDU(H2) 3X15", "ENCOLHIMENTO 3X15", "HIT ABS -> SO ABS"],
        "4": ["SUPINO INCLINADO 4X12", "SUPINO VERTICAL 4X12", "TRICEPS TESTA(W) 4X15", "TRICEPS COICE 4X12",
              "APOIO SOLO + TRICEPS CORDA 4X12", "VOADOR 4X12"]
    }

    if nometreino in treinos:
        st.write(f"Treino -> {nometreino}")
        st.write("Exercícios")
        for exercicio in treinos[nometreino]:
            st.write(f"{exercicio}")
    else:
        st.error("Treino não encontrado")

# Aplicativo Streamlit
st.title("*-----Sistema de Cadastro------*")

st.header("Cadastro")
cadastro()

st.header("Informações do Cliente")
informacoes_cliente()

tabelaimc = st.selectbox("Gostaria de ver a tabela de IMC?", ["Não", "Sim"])

if tabelaimc == "Sim":
    tabela_imc()

st.header("Calcular IMC")
peso = st.number_input("Digite seu peso (kg):", min_value=0.0, format="%.2f")
altura = st.number_input("Digite sua altura (m):", min_value=0.0, format="%.2f")

if st.button("Calcular IMC"):
    imc = calcular_imc(peso, altura)
    if imc:
        classificacao = classificacao_imc(imc)
        st.write(f"O seu IMC é: {imc:.2f}")
        st.write(f"Sua classificação é: {classificacao}")
    else:
        st.error("Altura deve ser maior que zero.")

st.header("Treinos")
treino_escolhido = st.selectbox('Digite o treino que você deseja:', ["1 - Costas", "2 - Pernas", "3 - Ombros", "4 - Peito"])

if st.button("Exibir Treino"):
    exibirtreino(treino_escolhido.split()[0])

repetir = st.radio("Deseja selecionar outro treino?", ["Não", "Sim"])
if repetir == "Não":
    st.write("Encerrando o programa.")
