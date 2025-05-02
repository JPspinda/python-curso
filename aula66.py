"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z):
    #definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
# soma(y=2, z=3, x=34)
soma(1, y=2, z=5) #todos os parâmetros que foram nomeados, os parâmetros que vierem depois terão que ser nomeados também
soma(z=32, x=9, y=8)
print(1, 2, 3, sep='-')