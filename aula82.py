# lista = [1, 23, 3, 435, 65, 3, 2, 34]
# lista.sort(reverse=True)

# print(lista)

lista = [
    {'nome': 'João', 'sobrenome': 'Spinda'},
    {'nome': 'Pedro', 'sobrenome': 'Paulino'},
    {'nome': 'Carlos', 'sobrenome': 'Oliveira'},
    {'nome': 'Eduardo', 'sobrenome': 'Guedes'},
]

def exibir(lista):
    for item in lista:
        print(item)

# lista.sort(key=lambda item: item['sobrenome']) #passando a função no sort(hey=) e retornando o item na função, .sort() muda a lista inteira
l1 = sorted(lista, key=lambda item: item['sobrenome'])#sorted copia a lista ordenada
l2 = sorted(lista, key=lambda item: item['nome']) #lambda é uma função sem nome

exibir(l1)
exibir(l2)