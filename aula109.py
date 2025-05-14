from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéstes'],
]

lista = [
    i for i in combinations(pessoas, 2)
]
# print_iter(combinations(pessoas, 2))
# print()
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
