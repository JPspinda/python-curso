string = 'luiz otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' você não pode fazer isso pois string é um tipo imutável, você não muda o valor da string com outravariável
print(string)
print(outra_variavel) #você conseguiu mudar pois mudou em outra variável, mas a 'string' continua immutável
print(string.capitalize()) #começa a string com letra maiúscula
print(outra_variavel.lower()) #há métodos específicos para cada valor, int, float e até bool
print(string.zfill(100)) #coloca a quantidade de zeros que foi colocada no parênteses na esquerda da string