variavel = 'Olá Mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:]) #fatia a string, pega só as caracteres que passamos pelo parametro
print(variavel[4:9]) #o número na frente é onde comeca e o do final é onde o índice termina
print(variavel[0:5])
print(variavel[-8:-1])
print(variavel[-5:-1])
print(variavel[1:9:5])#isso faz com que, o índice do começo é onde começa, o índice do meio é o onde termina e o do final é quantas casas pula
print(variavel[0:9:3])
print(variavel[-1:-10:-1])#inverte a string
print(variavel[::-1])#inverte a string também
print(variavel[::3]) #quando não tem nada ele conta do índice 0 até onde vai
print(variavel[0:len(variavel):3])
print(len(variavel[3])) #aqui a len só conta quantas caracteres tem no índice 3
print(len(variavel)) #a função len conta quantas caracteres têm
