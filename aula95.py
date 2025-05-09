try:
    print('ABRIR ARQUIVO') 
    # 8/0  
except ZeroDivisionError:
    print('DIVIDIU ZERO')
except NameError:
    print('NameError')
except IndexError:
    print('IndexError')
else: #ele será executado caso não aconteça nenhum erro no código
    print('NÃO DEU ERRO')
finally: #o finally será executado de todo jeito, mesmo que ocorreu algum problema
    print('FECHAR ARQUIVO')