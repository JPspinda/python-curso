"""
Herança Simples - Relações entre Classes
Associação - usa, Agregação - tem
Composição - É dono de, Herança - É um

Herança vs Composição

Classe principal (Pessoa)
    -> super class, base calss, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class
"""
# object
class Pessoa: # para herdar uma classe você pode colocar a "super classe" dentro dos parênteses
    cpf = '1234'
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__) # consigo ver o nome da classe com o último self

class Cliente(Pessoa):
        
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf Aluno'

# help(Foo)
c1 = Cliente('João', 'Spinda')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)

# help(Cliente)
# para não deixar o código muito complexo na herança, o bom seria deixar a herança em apenas uns 3 níveis