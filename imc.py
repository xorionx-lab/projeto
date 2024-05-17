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

