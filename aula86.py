lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
        
lista = [ #o lado esquerdo é exclusivo para variáveis, não coloca em nenhum outro lugar
    [(x, letra) for letra in 'Joao'] 
    for x in range(3)
]
print(lista)