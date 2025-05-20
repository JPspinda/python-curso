# def soma(a, b, /, x, y): # colocando a barra, não posso nomear nenhum dos argumentos anteriores, apenas os posteriores
#     print(a + b + x + y)

def soma(a, b, /, *, c, **kwargs): # no '*' é diferente, pois preciso nomear o argumento e nãoo deixá-lo apenas posicional
    print(a + b, kwargs)

soma(1, 2, c=3, nome= 'joao')

