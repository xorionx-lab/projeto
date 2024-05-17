print("*-----Sistema de Cadastro------*")

contador = 0
for contador in range(1,3):
    nome = str(input("Digite o nome para o cadastro: "))
    senha = int(input("Digite uma senha para o cadastro: "))
    csenha = int(input("Confirme a senha: "))

    if senha == csenha:
        print(f"Seja Bem-Vindo: {nome}")
        break
    else:
        print("Tente mais uma vez")
print("---------------------------\n")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("digite sua altura: "))
print("-------------------------------")
print(f"Esse é seu nome: {nome}")
print(f"Essa é sua idade: {idade}")
print(f"Essa é seu peso: {peso}")
print(f"Essa é sua altura: {altura}")

print("-----------------\n")
print("-------TABELA IMC-------")
def tabela():
    print("----Classificação IMC----")
    print("----IMC-----|-----Classificação----")
    print("Menor que 18.5 | Abaixo do peso")
    print("18.5 - 24.5 | Peso normal")
    print("25 - 29.9 | Peso normal")
    print("30 - 34.9 | Obesidade Grau I")
    print("35 - 39.9 | Obesidade Grau II")
    print("Maior que 40 | Obesidade Grau III")

tabelaimc = int(input("Gostaria de ver a tabela: 1 - Sim | 2 - Não: "))

if tabelaimc == 1:
    tabela()
else:
    print("ok")

def calcularimc(peso,altura):
    altura_imc = altura/1
    imc = peso/(altura_imc**2)
    return imc
def classificacaoimc(imc):
    if imc < 18.5:
        return "Abaixo peso"
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
print(f"O seu imc é: {calcularimc(peso,altura):.2f}")
print(f"Sua classificação é: {classificacaoimc(calcularimc(peso, altura))}")

print("--------TREINOS------------\n")

treinos = {
    "1":["GRAVITON (N) 4X10 |", "PUXADOR FRENTE (N) 4X12, 3X8 |", "PUXADOR INVERSO 4X12, 3X8 |", "REMADA CURVA (PRO) 4X12 | ", "ROSCA INVERSA POLIA 3X15|", "ROSCA SCOOT 4X12(FI) 2X8(UNI)|", "ELAVAÇÃO LATERAL(POLIA) 3X10+FALHA|", "HIT + ABS INFRA + AERÓBICO"],
    "2":["HACK MACHINE 4X 10,12,2X10|", "HAC 45 4X12, 3X10|", "AFUNDO 4X 1X10,1X12, 2X10|", "CADEIRA FLEXORA + PASSADA 4X12 , 15|", "CADEIRA EXTENSORA 4X ISO5' + 15|", "PANTURRILHA 3X20"],
    "3":["MANGUITOS AQUE|","DESENVOLVIMENTO 3X15|","CRUXIFIXO INVERSO 3X15|","ELEV.LAT PO.5X15|","DESENVOL HALT 3X15|","ADUCÇÃO+ABDU(H2) 3X15|","ENCOLHIMENTO 3X15|","HIT ABS -> SO ABS"],
    "4":["SUPINO INCLI 4X12|","SUP VERT 4X12|","TRICEPS TEST(W) 4X15|","TRICEPS COICE 4X12|", "APOIO SOLO + TRICEPS CORDA 4X12|", "VOADOR 4X12"]
}
def exibirtreino(nometreino):
    if nometreino in treinos:
        print(f"Treino -> {nometreino}")
        print("Exercicios")
        for exercicio in treinos[nometreino]:
            print(f"{exercicio}")
    else:
        print("Treino não encontrado")
while True:
    escolha = input('Digite o treino que você deseja -> 1 - Costas | 2 - Pernas | 3 - Ombros | 4 - Peito: ')
    escolha = escolha.strip() + ""

    exibirtreino(escolha)

    repetir = input("Deseja selecionar outro treino? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa.")
        break



