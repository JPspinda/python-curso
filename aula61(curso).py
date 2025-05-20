cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_1 = 0
for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0