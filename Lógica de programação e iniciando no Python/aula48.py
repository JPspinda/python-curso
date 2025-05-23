"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar Ler Alterar Deletar = lista[i] (CRUD)
"""

# #        +01234
# #        -54321
# string = 'ABCDE' #5 caracteres (len)
# #print(string[2])
# # print(bool(lista)) #se a lista estiver vazia é False
# # print(lista, type(lista))

# #        0      1      2      3  4
# #        -5     -4     -3    -2  -1
# lista = [123, True, 'João', 3.4, []] #list()
# print(type(lista[2]))
# print(type(lista[1]))
# print(lista[2].upper(), type(lista[2]))
# lista[-3] = 'Maria'
# print(lista[2])
# print(lista)

# lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50)
# lista.pop() #neste local do .pop() o último número da lista é o '50'
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3) #nesse caso é removido o valor do índice
# print(f'{lista} Item Removido: {ultimo_valor}')

# lista = [10, 20, 30, 40]
# lista.append('João')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c =  lista_a + lista_b
lista_a.extend(lista_b) #ele meche diretamente com a lista_a e não cria um novo elemento
print(lista_a)