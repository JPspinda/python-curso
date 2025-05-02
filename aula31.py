# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2)) id serve para ver a identidade da variável

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# print(passou_no_if, passou_no_if is None) #o 'is' é igual a comparação ==, porém com valores None voce usa is
# print(passou_no_if, passou_no_if is not None) #o 'is not' é igual a comparação !=

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')