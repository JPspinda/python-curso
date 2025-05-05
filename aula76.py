# pessoa = {
#     'nome': 'João Pedro',
#     'sobrenome': 'Spinda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 123}
#     ],
# }
# pessoa = dict(nome='João Pedro', sobrenome='Spinda')
# print(pessoa['nome']) #os colchetes conseguem acessar os valores do dicionário
# print(pessoa['sobrenome'])

# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])

pessoa = {
    
}

chave = 'nome'

pessoa[chave] = 'João Pedro'
pessoa['sobrenome'] = 'Spinda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', None)) com o .get(), se a chave existir, ele irá retornar a chave, se não, ele retornará None

if pessoa.get('sobrenome') is None:
    print('Não existe')

else:
    print('Existe')