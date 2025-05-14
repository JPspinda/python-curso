from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Joao', 'nota': 'C'},
    {'nome': 'Fernanda', 'nota': 'D'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'José', 'nota': 'D'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

# alunos = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
grupos = groupby(alunos_agrupados, key=ordena) #groupby agrupa os valores em grupos de valores e iteradores e eles precisar estar ordenados

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)