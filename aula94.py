# a = 18
# b = 0
# c = a / b
try:
    a = 18
    b = 0
    print(b[0])
    print('Linha 1'[100])
    print
    c = a / b
except ZeroDivisionError: # é sempre bom identificar os erros
    print('Dividiu por 0.')
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError):
    print('TypeError')
except Exception:
    print('Erro desconhecido.')
    
print('CONTINUAR')