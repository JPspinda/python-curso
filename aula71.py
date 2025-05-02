"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    print(args)
    total = 0
    for numero in args:
        # print('Total', total, numero)
        total += numero
        # print('Total', total)
    return total
    
soma1_2_3 = soma(1, 2, 3)
# print(soma1_2_3)

soma4_5_6 = soma(4, 5, 6)
# print(soma4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7   
outra_soma = soma(*numeros) #estamos "espalhando" os valores da tupla aqui dentro
print(outra_soma)

# print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))