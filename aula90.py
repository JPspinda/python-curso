# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo): #checa se o método exite no objeto
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)