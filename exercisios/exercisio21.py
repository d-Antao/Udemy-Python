lista_a =[10,2,3,40,5,6,7]
lista_b =[1,2,3,4]

def soma_lista(l1,l2):
    entrevalo_maximo = min(len(l1),len(l2))
    return[
        (l1[i]+l2[i]) for i in range(entrevalo_maximo)
    ]
    

print(soma_lista(lista_a,lista_b))

#ou para qualquer ligua de prog

lista_soma = []
for i in range(min(len(lista_a),len(lista_b))):
    lista_soma.append(lista_a[i]+lista_b[i])
    
print(lista_soma)

#ou
lista_soma2 =[]

for i,_ in enumerate(lista_b):
    lista_soma2.append(lista_a[i]+lista_b[i])
    
print(lista_soma2)

#ou

lista_soma3 = [x + y for x,y in zip(lista_a,lista_b)]
print(lista_soma3)

#ou para capeturar todos os valores

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]