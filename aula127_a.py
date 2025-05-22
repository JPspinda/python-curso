import json

CAMINHO_ARQUIVO = 'aula127(curso).json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    print('FAZENDO DUMP')
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        dado = json.dump(bd, arquivo, indent=2, ensure_ascii=False)
    
if __name__ == '__main__':
    fazer_dump()