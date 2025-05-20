# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome): # quando o 'def' está dentro da classe ele não é chamado de função, e sim de método, o primeiro parâmetro é sempre reservado para self
        self.nome = nome # o self é como se fosse a variável dentro da função
        self.sobrenome = sobrenome
    
p1 = Pessoa('João', 'Spinda')
# p1.nome = 'João'
# p1.sobrenome = 'Spinda'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.sobrenome)
print(p1.nome)

print(p2.sobrenome)
print(p2.nome)