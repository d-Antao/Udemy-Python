from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('Total é', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))

interiter = (cont for cont in range(1, 5))

listafilter = [{'nome': f'Produto {next(interiter)}','preco': item} for item in list(item*3.59 for item in [1, 2, 3, 5])]

print(reduce(lambda acumulador, item: round(item['preco'] + acumulador, 2), listafilter, 0))