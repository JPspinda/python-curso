# 0  1  2  3
# J  O  Ã  O
#-4 -3 -2 -1
# as letras estão em índices

# nome = 'João'
# print(nome[-3])
# print(nome[1]) # acessa a letra que está no índice
# print('a' in nome) # verifica se a letra ã está na str João
# print('ã' in nome)
# print('J' not in nome) # verifica se h´ra alguma letra que não está na str João
# print('Q' not in nome)
nome = input('Digite seu nome: ')
encontrar = input('Digite a letra que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')