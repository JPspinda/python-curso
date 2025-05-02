hora = input('Informe a hora de agora: ')
hora_int = int(hora)
bom_dia = hora_int <= 11
boa_tarde = 12 <= hora_int <= 17

if bom_dia:
    print('Bom dia')
elif boa_tarde:
    print('Boa Tarde')
else:
    print('Boa noite')