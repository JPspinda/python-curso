from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
# def porcentagem(porcentagem):
#     def aumentar_porcentagem(valor):
#         return round(valor * porcentagem, 2)
#     return aumentar_porcentagem
    
# dez_porcento = porcentagem(1.1)  
    
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)
    
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

aumentar_dez_porcento = partial( #a partial cria uma 'closure' na função, cria uma função com um valor padrão
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }

#map para mapear dados
novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))
# novos_produtos = (x for x in produtos)

print_iter(produtos)
print_iter(novos_produtos) #o iterator 'map' esgota, então se você listar em um print ele fica vazio

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

# print(novos_produtos)
# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))
# print(isinstance(novos_produtos, GeneratorType))