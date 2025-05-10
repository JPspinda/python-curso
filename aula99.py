import importlib

import aula99_m

print(aula99_m.variavel)

for i in range(10):
    importlib.reload(aula99_m) #só existe uma instância no código inteiro, ele não importa mais de 1 vez
    
print('Fim')