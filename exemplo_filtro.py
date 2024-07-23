# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):
    return produto['preco'] > 100


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]
novos_produtos = filter(
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)


#ou-------------------------------------------------------------------------------------------------------------------------------------

def print_iter(iterable):
    print(*iterable, sep='\n')
    print('')

produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]

interiter = (cont for cont in range(1, 5))
listafilter = [{'nome': f'Produto {next(interiter)}','preco': item} for item in list(item*3.59 for item in [1, 2, 3, 5])]

print('Produtos de Produtos: ')
print_iter(produtos)

print('Produtos da Lista Filter: ')
print_iter(listafilter)

print('Produtos filtrados por list Comprehension: ')
print_iter(list({**dicionario} for dicionario in produtos if dicionario['preco'] > 50))
print('')

print('Produtos da listafilter filtrados por filter: ')
print_iter(list(filter(lambda dicionario: dicionario['preco'] > 10, listafilter)))
