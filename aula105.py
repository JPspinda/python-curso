def fabrica_de_decoradores(a=None, b=None, c=None):
    
    def fabrica_de_funcoes(func):
        print('fabrica_de_funcoes 1')
        
        def aninhada(*args, **kwargs):
            print('Parametros do decorador', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y): #é como se eu estivesse transformando a função soma com a aninhada
    return x + y

multiplica = fabrica_de_decoradores()(lambda x, y: x * y)
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)