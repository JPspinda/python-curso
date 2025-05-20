string = 'Qualquer valor'

i = 0
while i < len(string):
    letra = string[i]

    # break se tiver um break dentro do while o else não é executado

    print(letra)
    i += 1
else:
    print('o Else foi executado.')
print('Fora do while.')