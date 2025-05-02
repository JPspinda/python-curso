"""
iterável -> string, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me intrega o iterador
"""
# texto = iter('Luiz') #__iter__()
# #precisa ter o iter para o next funcionar
# print(next(texto)) #__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))

#for letra in texto (aqui ele já está solicitando o iterador)
texto = 'Luiz' #iteravel
# iterador = iter(texto) #iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break
#     isso tudo é o que o for faz, pois a letra é o "next" e o texto é o iterador do iterável

for letra in texto:
    print(letra)