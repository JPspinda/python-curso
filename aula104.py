def criar_funcao(func):
    
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
            
            resultado = func(*args, **kwargs)
            resultado += "QUAL"
            print(f'O seu resultado foi {resultado}')
            print('OK, agora você foi decorada')
        return resultado
    return interna    


@criar_funcao #você consegue usar oa função 'criar_função' na função 'invrte_sring', como se "mesclace" as duas funções
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

invertida = inverte_string('João')
print(invertida)