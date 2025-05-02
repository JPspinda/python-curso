"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    if x > 10:
        return 10 #retorna o valor da função

    return x + y        
    # print(x + y) qualquer código dentro da função após o ruturn não é executado



# variavel = soma(1, 2) #essa variável retorna o valor None
# variavel = int('1')
soma1 = soma(2, 2) #se não tiver o return, mesmo que tenha os valores, a função retornará None
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 2))