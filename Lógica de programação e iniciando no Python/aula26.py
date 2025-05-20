variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: <10}.')# 10 espaços < - para a direita
print(f'{variavel: >10}') # 10 espaços > - para esquerda
print(f'{variavel: ^10}') # 10 espaços ^c- para ambos os lados
print(f'{1000.1342399128:+,.2f}')# para aparecer apenas 2 casa decimais, mostra se é positivo ou negativo e adiciona a vírgula na casa de milhar
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}') # !r !a !s -> conversion flags