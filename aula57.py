"""
Listas de Listas e seus índices
"""
salas = [
    #0           1
    ['Maria', 'Helena'], #0
    #0
    ['Elaine'], #1
    #0         1         2 
    ['Luiz', 'João', 'Eduarda' ] #2
]

# print(salas[1][0]) #primeiro é o índice da lista e o segundo o valor da lista que está dentro da lista
# print(salas[0][1])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)