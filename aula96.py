# print(123)
# raise ValueError('Deu erro') #o raise ele 'lança' um erro que você der mesmo não tendo nenhum
# print(456)
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return True

def deve_ser_int_ou_float(n, d):
    tipo_n = type(n)
    if not isinstance((n, d), (float, int)):
        raise TypeError(
            f'{(n, d)} deve ser int ou float',
            f'{tipo_n.__name__} enviado.'
        )    

def divide(n, d):
    deve_ser_int_ou_float(n, d)    
    nao_aceito_zero(d)
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    
    return n / d
    
print(divide('8', 0))