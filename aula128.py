class Pessoa:
    ano = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod # faz com que eu possa chamar meu método na classe sem precisar do parâmetro 'self'
    def metodo_de_classe(cls):
        print('Hey')
    
    @classmethod 
    def criar_com_50_anos(cls, nome): # o 'cls' é como se fosse a classe, igual quando o self é a variável
        return cls(nome, 50) # retorna a classe como o nome e com 50 anos
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# p1.metodo_de_classe()
# Pessoa.metodo_de_classe()
p1.metodo_de_classe()