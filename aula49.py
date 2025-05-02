"""
Cuidados com dados mutáveis
= - Copiado o valor (imutáveis)
= - aponta para o mesmo valor na memórial (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #com essa função a lista_b não vai ser mudada

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)