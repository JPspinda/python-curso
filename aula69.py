"""
Escopo de função em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde tod código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem alcançar.
Cada função tem seu próprio escopo.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz uma variável do escopo externo
ser a mesma do escopo interno.
"""
x = 1
def escopo():
    # global x # a palavra 'global' permite que a função edite a variável fora da função, porém o valor se altera apenas depois que a função é chamada
    x = 10 # esse novo 'x' não é o mesmo 'x' definido no começo do código
    print(x)
    
    def outra_funcao():
        # global x
        x = 11
        y = 2 #a função escopo() não tem acesso a variável 'y'
        print(x, y)
        
    outra_funcao()
    print(x)
    
    
print(x)
escopo()
print(x)