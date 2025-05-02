cpf = input('Informe o seu CPF: ')
cpf = cpf.replace('.','',2) #funciona assim, objeto_string('valor a ser substituído', 'novo valor atribuído', quantidade de vezes que será substituido)
cpf = cpf.replace('-','')
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
total_numeros_1 = 0

for digito_1 in nove_digitos:
    digito_int = int(digito_1)  
    total_numeros_1 += digito_int * contador_regressivo_1
    contador_regressivo_1 -= 1
    
primeiro_digito = (total_numeros_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print(primeiro_digito)