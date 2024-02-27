# Média:
# Faça um programa que pede para o usuário
# escrever 3 notas, calcule a média e mostre se ele foi
# aprovado (acima de 7) ou reprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <= 10:
    print("Aprovado.")
elif media < 7 and media >= 0:
    print("Reprovado.")
else:
    print("Digite uma nota válida entre 0 e 10.")

# -------------------------------------------#
# Semáforo:
# Faça um programa que pede para o usuário
# escrever uma cor e mostre “Pare” se for vermelho,
# “Atenção” se for amarelo “Acelera” se for verde e
# “Cor inválida” se for qualquer outra

cor = str(input("Digite aqui uma cor (verde, vermelho ou amarelo): ")).lower()

if cor == "vermelho":
    print("Pare!")
elif cor == "verde":
    print("Acelere!")
elif cor == "amarelo":
    print("Atenção!")
else:
    print("Digite uma cor válida (verde, amarelo ou vermelho.)")

# -------------------------------------------#
# Dia da semana:
# Faça um programa que pede pro usuário escrever
# um número inteiro entre 1 e 7 e mostre o dia da
# semana respectivo ao número digitado (1 -
# domingo, 2 - segunda e etc)

menu = int(
    input(
        """
            Escolha o dia da semana:
            1 - Domingo
            2 - Segunda-feira
            3 - Terça-feira
            4 - Quarta-feira
            5 - Quinta-feira
            6 - Sexta-feira
            7 - Sábado                 
"""
    )
)

if menu == 1:
    print("O dia escolhido foi domingo.")
elif menu == 2:
    print("O dia escolhido foi segunda-feira.")
elif menu == 3:
    print("O dia escolhido foi terça-feira.")
elif menu == 4:
    print("O dia escolhido foi quarta-feira.")
elif menu == 5:
    print("O dia escolhido foi quinta-feira.")
elif menu == 6:
    print("O dia escolhido foi sexta-feira.")
elif menu == 7:
    print("O dia escolhido foi sábado.")
else:
    print("Opção inválida, digite um número inteiro entre 1 e 7")

# -------------------------------------------#
# Maior de idade:
# Faça um programa que pergunte qual ano o
# usuário nasceu e mostre na tela se ele é ou não
# maior de idade

ano_nascimento = int(input("Digite o ano que você nasceu: "))
idade = 2024 - ano_nascimento

if idade >= 18:
    print("É maior de idade!")
else:
    print("É menor de idade")

# -------------------------------------------#
# Maior de três:
# Faça um programa que pede 3 números inteiros
# para o usuário e mostra na tela qual o maior dos
# três ou se ele são iguais

num1 = int(input("Digite aqui o primeiro número: "))
num2 = int(input("Digite aqui o segundo número: "))
num3 = int(input("Digite aqui o terceiro número: "))

if num1 == num2 and num2 == num3:
    print("Os números são iguais.")
else:
    numero_maior = num1
    if num2 > numero_maior:
        numero_maior = num2
    if num3 > numero_maior:
        numero_maior = num3
    print(f"O maior número é o {numero_maior}")
