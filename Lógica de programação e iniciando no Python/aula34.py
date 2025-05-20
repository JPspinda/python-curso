condicao = True

while condicao: #o while repete o bloco de código enquanto a condição for verdadeira, True
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome =='sair':
        break

print('Acabou')