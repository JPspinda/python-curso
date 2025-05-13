# print(globals())
# def fora(x):
#     a = x
    
#     def dentro():
#         # print(locals()) com globals() consigo ver as variáveis globais, com locals, varáveis locais
#         # print(dentro.__code__.co_freevars)
#         return a
    
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar=''):
        nonlocal valor_final        
        valor_final += valor_a_concatenar # eu só consigo ler o valor da variável fora do escopo, e não mudar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)