"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite') 
"""
a função criar_saudacao está retornando apenas a função saudar
e não o escopo dela, porém como os dados, saudacao e nome, estão salvos
porque foram passados na hora da função criar_saudacao, então o que
está acontecendo, como a criar_saudacao retorna apenas a função saudar
é como se a virável estivesse assumino o valor da função saudar()
já com os valores 'saudacao' e 'nome' e para executar basta colocar 
os parênteses
"""
for nome in ['Maria', 'João', 'Pedro']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))