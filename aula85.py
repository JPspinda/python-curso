"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis
"""
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero * 2)
# print(lista)
lista = [
    numero * 2
    for numero in range(10)
] #passando o parâmetro a esquerda ele adiciona na lista
# print(list(range(10)))
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} #o 'if' também em a esquerda do for
    for produto in produtos
]

# p(novos_produtos)

# print(novos_produtos)
# print(*novos_produtos, sep='\n')

# lista = [1, 2, 4, 6]
# nova_lista = [
#     numero * 2 for numero in lista
# ]

# print(nova_lista)

lista = [n for n in range(10) if n < 5] #filtra quais dados podem entrar na lista
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} #o 'if' também em a esquerda do for
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 #exclui os que são menores que 10
]
p(novos_produtos)