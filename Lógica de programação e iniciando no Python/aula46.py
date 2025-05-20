for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é igual a 8, seu else não executará')
        break #quando eu chamo o break o else não é executado como se fosse o"if"

    for j in range(1, 4): # vai pegar do 1 ao 2 pois o 3 não entra
        print(i, j)
else: 
    print('for completo com sucesso')