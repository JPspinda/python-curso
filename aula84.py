a, b = 1, 2
a, b = b, a
print(a, b)

# # a, b = pessoa.items()
# (a1, a2), (b1, b2) = pessoa.items() #o 'items()' transforma as chaves em tuplas, com isso conseguimos desempacotar os itens da tupla
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# pessoa_completa = {**pessoa, 'nome': 1}
pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)
def mostro_argumentos_nomeados(*args, **kwargs): #sempre que for algumentos nomeados é o **kwargs que empacota argumentos nomeados
    print('NÃO NOMEADOS', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
    
# mostro_argumentos_nomeados(1, 2, 3, nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)