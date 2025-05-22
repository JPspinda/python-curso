import json

def salvar(classe, caminho_arquivo):
    dado = classe
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dado = json.dump(dado, arquivo, indent=2, ensure_ascii=False)
    return dado

caminho = 'aula127.json'

class Pessoa:
    ano_atual = 2025
    
    def __init__(self, nome, idade, comida_fav, gosto, hobbie):
        self.nome = nome
        self.idade = idade
        self.comida_fav = comida_fav
        self.gosto = gosto
        self.hobbie = hobbie
        # self.ano_atual = 100
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 18, 'Strogonoff', 'Jogar Bola', 'Guitarra')
p2 = Pessoa('Maria', 20, 'Omelete', 'Ler', 'Tricô')
salvar(vars(p1), caminho)
salvar(vars(p2), caminho)