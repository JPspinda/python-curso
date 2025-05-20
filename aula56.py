"""
split e join com list e str
split - divide uma string
join - une uma str
"""
frase = '    Olha só que,    coisa interessante   '
lista_frases_cruas = frase.split(',') #separa em uma lista
lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())#'strip' 'corta' os espaços do começo e no fim, 'rstrip' corta apenas da direita, 'lstrip' apenas da esquerda


# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases) #coloca um item no meio da string, funciona apenas em string, listas e tuplas
print(frases_unidas)