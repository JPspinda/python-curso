numero_str = input('Vou dobrar o número que você digitar: ')
# print(numero_str.isdigit()) #verifica se digitaram número, apenas números, sem pontos e nada

try: #o try e except é tipo if e else, porém se der erro dentro da sintáxe ele não para e sim pula para o except
    print('STR:', numero_str)
    numero_float = float(numero_str) #se ocorrer um erro aqui, ele pula para o except
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número.')
#try tenta executar o código, except é quando ocorre o erro

# if numero_str.isdigit():

# else:
#     print('Isto não é um número')