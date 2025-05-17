import os

caminho_arquivo = r'C:\\Users\\Ample Telecom\\Desktop\\python\\' # caminho completo no windows, em vez de usar 1 barra invertida, precisa usar 2
caminho_arquivo += 'aula116.txt' # busca os arquivos ou da pasta que você está ou fora

# # arquivo = open(caminho_arquivo, 'w') # open() eu paço dois parâmetros, primeiro o caminho do arquivo e segundo o modo que vai utilizar no arquivo: 'r', 'w', 'a', 'x', 'b', 't', '+'

# # arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo: #com o with o arquivo será aberto e fechado sem precisar do .close()
#     print(type(arquivo))
#     arquivo.write('Linha 1\n') # write()escreve uma coisa no arquivo
#     arquivo.write('Linha 2\n') # com o '+' eu consigo fazer com que o arquivo consiga ler e escrever
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n') # writelines() escreve várias linhas
#     )
#     arquivo.seek(0, 0) # o seek() funciona para você voltar no arquivo para conseguir ler
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='') # o readline() lê apenas 1 linha por vez
#     print(arquivo.readline().strip()) #.strip() retira todos os espaços da string
#     print(arquivo.readline().strip())
#     print('READLINES')
#     for linha in arquivo.readlines(): # readlines() consigo ler com um
#         print(linha.strip())
    
# with open(caminho_arquivo, 'r') as arquivo: 
#     print(arquivo.read())

with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo: # o modo 'a' adiciona no final do arquivo, o modo 'w' ele apaga tudo o que está no arquivo e depois escreve
    arquivo.write('Atenção\n') #o windown não pega os caracteres especiais 'ç' e '~', porém com o encoding= você consegue fazer com que os caracteres sejam certos
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo) # os.unlink() ou os.remove() apaga o arquivo criado
os.rename(caminho_arquivo, 'Aula116-2.txt') # os.rename() renomeia o arquivo