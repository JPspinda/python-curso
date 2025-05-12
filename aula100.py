#cria um arquivo na raíz que é o seu main e importa tudo o que você quiser nesse main
# from sys import path

# import aula100_package.modulo
# from aula100_package import modulo
# from aula100_package.modulo import soma_do_modulo
# from aula100_package.modulo import *

# # print(*path, sep='\n')
# print(soma_do_modulo(2, 2))
# print(aula100_package.modulo.soma_do_modulo(2, 2))
# print(modulo.soma_do_modulo(2, 2))
# print(variavel)
# print(nova_variavel)
# from aula100_package.modulo import soma_do_modulo
# from aula100_package.modulo_b import *args
# print(__name__)
# print(soma_do_modulo(2,2))

#o arquivo __init__ é importado com o package, ele faz o package ser importado
from aula100_package import soma_do_modulo, fala_oi

print(soma_do_modulo(2, 3))
fala_oi()