# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# #if condição: True
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação curto circuito
#na avaliação 'and' o que prevalece é o valor False, na avaliação 'or', o que prevalece é o valor True
# print(True or False)
# print(True and 'abc' and 10 and 0)
# print(False or False or False or 0 or 0.0 or '' or 'abc')
# senha = False or 10 or 0 or 0.0 or ''
# print(senha)

senha = input('Digite sua senha: ') or 'Sem senha' #se deixar vazio o input ele conta como False e vai para o outro valor True
print(senha)