# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo)
#     ]

# print(zipper(l1, l2))
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2))) #usa o valor da lista menor
print(list(zip_longest(l1, l2, fillvalue='Sem Cidade'))) #usa o valor da lista maior

def soma_de_lista(lista1, lista2):
    # intervalo = min(len(lista1), len(lista2))
    resultado = [x + y for x, y in zip(lista1, lista2)]
    # for i in range(intervalo):
    #     soma = lista1[i] + lista2[i]
    #     resultado.append(soma)
        
    return resultado
        

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4]
print(soma_de_lista(l1, l2))
