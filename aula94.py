# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[100])
    print
    c = a / b
except ZeroDivisionError as e: # é sempre bom identificar os erros
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as error: #a variável 'error' está pegando a mensagem explicando qual erro ocorreu
    print('TypeError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)# usando isso você consegue saber o tipo do erro
except Exception:
    print('Erro desconhecido.')
    
print('CONTINUAR')