nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

if nome  and idade  :
    print(f"O nome digitado foi {nome}")
    print(f"o seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print(f"O nome {nome} contém espaços.")
    else:
        print(f"O nome {nome} não contém espaços.")
    print(f"o seu nome contem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[len(nome)-1]}")

else:
    print(f"Desculpe, voce deixou campos vazios")