import json

def print_dict(dict):
    for especificacao, valor in dict.items():
        print(f'{especificacao}: {valor}')

def ler(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe.')
    print_dict(dados)

dict = {'nome': 'João', 'idade': 18, 'comida_fav': 'Strogonoff', 'gosto': 'Jogar Bola', 'hobbie': 'Guitarra'}

caminho = 'aula127.json'
ler(caminho)