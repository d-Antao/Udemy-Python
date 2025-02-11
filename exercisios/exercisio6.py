"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""



numero = input("Digite um número: ")
try:
    if int(numero) % 2 == 0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é ímpar")
except:
    print("Desculpe, você não digitou um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Que horas são? ")
try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except:
  print("Desculpe, você não digitou uma hora válida.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
""" 
    
nome = input("Qual o seu nome? ")
condicao = nome.isdigit()
if not condicao:
    if len(nome) <= 4:
        print("Seu nome é curto")
    elif len(nome) > 4 and len(nome) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Desculpe, você não digitou um nome válido.")
    