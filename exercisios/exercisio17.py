import copy



produtos = [
    {'nome': 'produto 5', 'preço': 10.00},
    {'nome': 'produto 1', 'preço': 22.32},
    {'nome': 'produto 3', 'preço': 10.11},
    {'nome': 'produto 2', 'preço': 105.87},
    {'nome': 'produto 4', 'preço': 69.90},
]

def aumento_10(produtos):
    novos_produtos = copy.deepcopy(produtos)
    for produto in novos_produtos:
        produto['preço'] = round(produto['preço']*1.10, 2)
    print(*novos_produtos,sep='\n')

def ordene_nome_decrescente(produtos):
    produtos_odenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda item : item['nome'], reverse=True)
    print(*produtos_odenados_por_nome,sep ='\n')

def ordene_preco_crescente(produtos):
    produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda item : item['preço'])
    print(*produtos_ordenados_por_preco,sep='\n') 

aumento_10(produtos)
print('---------------------------------------')
ordene_nome_decrescente(produtos)
print('---------------------------------------')
ordene_preco_crescente(produtos)
print('---------------------------------------')
print(*produtos,sep='\n')