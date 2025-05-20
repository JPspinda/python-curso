#       012345678910
nome = input('Digite seu nome: ')
# print(nome[-11]) 

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'

    indice += 1

novo_nome += '*'
print(novo_nome)