a = 'AAAAA'
b = 'BBBBBBBB'
c = 1.1
string = 'a = {nome1} b = {nome2} c = {nome3:.2f} {nome1}'
formato = string.format(nome1=a, nome2=b, nome3=c,)

print(formato)

nome = 'João Pedro'
peso = 95
altura = 1.76
imc = peso / (altura * altura)

linha = '{} tem {} de altura, pesa {} quilos e seu IMC é {:.2f}'.format(nome, altura, peso, imc)

print(linha)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))