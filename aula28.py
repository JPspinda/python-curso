nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print('Você digitou nada ou deixou um campo aberto.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

# if nome or idade: desse jeito também daria certo
#     print(f'Seu nome é {nome}')
#     print(f'Seu nome invertido é {nome[::-1]}')

#     if ' ' in nome:
#         print('Seu nome tem espaços')
#     else:
#         print('Seu nome não tem espaços')

#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A última letra do seu nome é {nome[-1]}')
# else:
#     print('Você digitou nada ou deixou um campo aberto.')