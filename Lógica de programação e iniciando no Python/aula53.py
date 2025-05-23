"""
enumerate - enumera iteráveis (indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = list(enumerate(lista)) #entrega o iterador da lista e cria uma tupla com o índice e o nome

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')