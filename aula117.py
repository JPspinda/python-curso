import json

pessoa = {
    'nome': 'João Pedro',
    'sobrenome': 'Spinda',
    'endereços': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (5, 3, 7, 12),
    'dev': True,
    'nada': None,
    # 'ssss': {1, 2, 3}  # as estruturas do set() não consguem ser armazenadas em json
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, # faz o dump em uma string # utilizando o ensure_ascii=False faz com que os caracteres especiais fiquem certos
              indent=2) # o indent= formata o arquivo
    
# with open('aula117.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     # print(pessoa)
#     # print(type(pessoa))
#     print(pessoa['nome'])