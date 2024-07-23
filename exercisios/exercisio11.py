import os
lista = []
while  True:
    print('selecione uma opção')
    inserir = input('[i]nserir , [a]apagar, [l]istar: ')
    inserir = inserir.lower()
    
    if inserir == 'i':
        os.system('cls')
        lista.append(input('valor: '))
    elif inserir == 'a':
        try:
            indice = int(input('escolha o indice para apagar: '))
            lista.pop(indice)
        except ValueError:
            print('indice invalido apenas numeros inteiros')
        except IndexError:
            print('indice nao existe na lista')
        except Exception:
            print('erro desconhecido')
        
    elif inserir == 'l':
        os.system('cls')
        for indice, valor in enumerate(lista):
            print(indice, valor)
            
    else:
        os.system('cls')
        print('opção invalida')
        continue
            