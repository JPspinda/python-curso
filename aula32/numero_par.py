numero_par_impar = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_par_impar)
    saber_par_impar = numero_int % 2 == 0
    if saber_par_impar:
        print(f'{numero_int} é um número par')
    else:
        print(f'{numero_int} é um número ímpar')
except:
    print('Isso é um número flutuante ou não é um número.')

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')

# else:
#     print('Você não digitou um número inteiro')