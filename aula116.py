caminho_arquivo = r'C:\\Users\\Ample Telecom\\Desktop\\python\\' # caminho completo no windows, em vez de usar 1 barra invertida, precisa usar 2
caminho_arquivo += 'aula116.txt' # busca os arquivos ou da pasta que você está ou fora

# # arquivo = open(caminho_arquivo, 'w') # open() eu paço dois parâmetros, primeiro o caminho do arquivo e segundo o modo que vai utilizar no arquivo: 'r', 'w', 'a', 'x', 'b', 't', '+'

# # arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo: #com o with o arquivo será aberto e fechado sem precisar do .close()
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('READLINES')
#     for linha in arquivo.readlines():
#         print(linha.strip())
    
# with open(caminho_arquivo, 'r') as arquivo: 
#     print(arquivo.read())

with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    
with open(caminho_arquivo, 'b') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )