# s1 = set('Joao')
# s1 = {'João', 1, 2, 3} #o "set" não garante a ordem dos dados e ele não repete os valores, ele não irá repetir o 'o' de 'João
# print(s1, type(s1))
# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1) #remove os valores a mais
# s1 = s1 = {1, 2, 3, (1, 2, 3),} #o set não aceita variáveis mutáveis, tuplas são aceitas
#set não tem índice
# print(3 in s1)
# for numero in s1:
#     print(numero)

s1 = set()
s1.add('João')
s1.add(1)
s1.update(('Olá Mundo', 1, 2)) #no caso do update, ele itera os caracteres da string, porém ele deixa junto caso passar outro valores
# s1.clear() #limpa o set inteiro
s1.discard('Olá Mundo')
s1.discard('João')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #o '|' une os dois sets em 1
s3 = s1 & s2 #o '&' faz a interseção os dois sets em 1, deixa apenas os números iguais dos sets
s3 = s2 - s1 #o '-' faz a diferença os dois sets, o da esquerda é o que vai restar dos sets
s3 = s1 ^ s2 #o '^' faz a diferença simétrica dos sets, os que estão presentes apenas em um dos sets
print(s3)