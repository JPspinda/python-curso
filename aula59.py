# Desempacotamento em chamadas
# de métodos e funções
string = 'ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #0           1
    ['Maria', 'Helena'], #0
    #0
    ['Elaine'], #1
    #0         1         2 
    ['Luiz', 'João', 'Eduarda' ] #2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ')

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista) # o * separa os elementes das variáveis
# print(*string)
# print(*tupla)

print(*salas, sep='\n') #end='', sep=''