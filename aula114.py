# import sys
# sys.setrecursionlimit(1004) # edito o limite da call stack

# def recursiva(inicio=0, fim=10):
#     # Caso base
#     if inicio >= fim:
#         return fim
    
#     print(inicio, fim)
#     #Caso recursivo
#     # Contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim) # nós estamos fazendo um laço na função que armazena na call stack
# # o limite da call stack é 1000

# print(recursiva())  

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n - 1)
    
print(factorial(5))