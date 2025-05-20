"""
Iterável -> str, range, etc (__iter__)
"""

# numeros = range(10) #range(stop) começa sempre do 0
# numeros = range(5, 10) #range(start, stop)
# numeros = range(0, -20, -1) #range(start, stop, step)
numeros = range(0, 100, 14) #range(start, stop, step)

for numero in numeros:
    print(numero)