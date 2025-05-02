"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos)
e retorna um valor específico.
Por padrão, funções em Python retornam None (nada).
"""


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')

# def imprimir(a, b, c):
#     print(a, b, c)
    
# imprimir(1, 2, 3) #Os parâmetros precisam ser 'passados' senão não executa a função
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')
    
saudacao('João Pedro')
saudacao('Maria')
saudacao('Luiz')
saudacao()