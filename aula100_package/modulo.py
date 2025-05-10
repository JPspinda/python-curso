__all__ = [
    'variavel',
    'soma_do_modulo',
    'nova_variavel',
    'fala_oi',
] #o '__all__' ela faz com que a importação * importe 
from aula100_package.modulo_b import fala_oi

variavel = 'Alguma coisa'

def soma_do_modulo(x, y):
    return x + y

nova_variavel = 'oi'
fala_oi()