lista = ['maria', 'joao', 'pedro', 'ana']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
#ou
for nome in lista:
    print(nome,lista.index(nome))

#ou
lista_enumerada = enumerate(lista)
for indice in lista_enumerada:
    print(indice)

#ou 
for indice in enumerate(lista):
    print(indice)