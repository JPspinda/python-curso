# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2] #no caso de valores mutáveis, no caso da lista e dos dicts eles não irão criar um nova lista
# }

# # d2 = d1.copy() 
# d2 = copy.deepcopy(d1) #com o deepcopy() será copiado tudo, tanto imutáveis quanto mutáveis

# d2['c1'] = 100 #alterando o 'd2' altera juntamente o 'd1', porém, se usado o .copy() será dois dicionário diferentes
# d2['l1'][1] = 99999
# print(d1)
# print(d2)

# pessoa.setdefault('idade', 0) # "cria" uma chave com um valor padrão para não dar erro, porém caso tiver uma chave, ele não será executdo
# print(pessoa['idade'])
# print(len(pessoa)) #retorna a quantidade de chaves, não conta chaves repetidas
# print(list(pessoa.keys())) #retorna as chaves do dicionário
# print(list(pessoa.values())) #retorna os valores das chaves
# print(list(pessoa.items())) #retorna a chave e o valor


# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

p1 = {
    'nome': 'João Pedro',
    'sobrenome' : 'Spinda',
}

# nome = p1.pop('nome') #elimina uma chave do dicionário que passar no parêntesis
# ultima_chave = p1.popitem() #elimina sempre a última chave do dicionário
# print(ultima_chave)
# p1.update({ # edita e cria uma nova chave
#     'nome': 'Novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
tupla = ('nome', 'novo valor'), ('idade', 30), #tem sempre q deixar a vírgula na tupla
lista = [['nome', 'outro valor'], ['idade', 30]]
p1.update(lista)
print(p1)