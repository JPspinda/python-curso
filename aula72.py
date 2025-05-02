def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(num):
    num_int = int(num)
    multiplo_dois = num_int % 2 == 0
    if multiplo_dois:
        return f'{num} é um número par.'

    return f'{num} é um número ímpar.'
    
mult = mult(2, 2, 2)
numero = par_impar(input('Digite um número: '))
print(mult)
print(numero)