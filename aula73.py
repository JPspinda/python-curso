"""
Higher order Functions
Funções de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao #nesse caso o nome da função "saudacao" será agora "saudacao_2"
print(executa(saudacao, 'Bom dia', 'João'))
print(executa(saudacao, 'Boa noite', 'Maria'))