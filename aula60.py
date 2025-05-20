"""
Operação ternária (condicional em uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro variavel'
# print(variavel)
# digito = 1 # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
print('Valor' if False else 'Outro Valor' if True else 'Fim')