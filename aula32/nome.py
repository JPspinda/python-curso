nome = input('Insira seu nome: ')
tamanho_nome = len(nome)
nome_pequeno = tamanho_nome <= 4
nome_normal = tamanho_nome == 5 or tamanho_nome == 6

if nome_pequeno:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')