# try: 
#     import sys
#     sys.path.append('C:/Users/Ample Teleco/Desktop/python')
# except ModuleNotFoundError:
#     ...
# import aula98_m

# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')

import aula98_m
from aula98_m import soma, variavel_mod

# print('Esse módulo se chama', __name__)
print(aula98_m.variavel_mod) #estou chamando a variável que está na aula98_m
print(variavel_mod)
print(soma(2, 1))
print(aula98_m.soma(2, 1))