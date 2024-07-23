# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# # Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import copy
from itertools import zip_longest

regiao =['Salvador', 'Ubatuba', 'Belo Horizonte']
sigla = ['BA', 'SP', 'MG', 'RJ']


def qual_maior_lista(l1=None,l2=None):
    lis1 = []
    lis2 = []
    if len(l1)< len(l2):
        lis1 = copy.deepcopy(l1)
        lis2 = copy.deepcopy(l2)
    else:
        lis1 = copy.deepcopy(l2)
        lis2 = copy.deepcopy(l1)
    
    return lis1,lis2




def unir_pelo_menor(l1,l2):
    lis1,lis2 = qual_maior_lista(l1,l2)  
    lis_unida =[]
    for num in range(len(lis1)):
        lis_unida.append((lis1[num],lis2[num]))

    return lis_unida
print(unir_pelo_menor(sigla,regiao))     


#ou

def ziper(lista1,lista2):
    intervalo_maximo = min(len(lista1),len(lista2))
    return [
        (lista1[i],lista2[i]) for i in range(intervalo_maximo)
    ]
    

print(ziper(regiao,sigla))

#ou 

print(list(zip(regiao,sigla))) #apartir da menor lista
print(list(zip_longest(regiao,sigla,fillvalue='Sem região'))) #apartir da maior lista 