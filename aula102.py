# def multiplicador(b):
#     def multiplica(a):
#         return a * b
        
#     return multiplica

# duplicar = multiplicador(2)
# print(duplicar(3))

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x): #isso "retarda" a execução da função
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
print(soma_com_cinco(10))
print(multiplica_por_dez(10))