# import sys

# platform = 'A MINHA'
# print(sys.platform) #consigo ver o kernel do sistema
# print(platform)

# from sys import exit, platform 

# platform = 'A MINHA' #se eu criar variáveis com os nomes dos objetos que eu importei ele irão assumir o valor da variavel
# print(platform)

# import sys as s
# sys = 'alguma coisa'
# print(s.platform)

# from sys import platform as pt, exit as ex
# print(pt)

#má prática
from sys import *

print(platform)
print(exit)
