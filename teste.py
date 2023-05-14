cpf = '54843756067'

nove_digitos = cpf[:9]

cont = 10

soma_1 = 0

# cálculo do primeiro dígito verificador
for numero in nove_digitos:
    soma_1 += int(numero) * cont    
    cont -= 1

digito1 = (soma_1 * 10) % 11

if digito1 == 10:
    digito1 = 0

dez_digitos = cpf[:9] + str(digito1)

soma_2 = 0
cont_1 = 11

# cálculo do segundo dígito verificador
for numero in dez_digitos:
    soma_2 += int(numero) * cont_1
    cont_1 -= 1

digito2 = (soma_2 * 10) % 11

if digito2 == 10:
    digito2 = 0

cpf_calculo = f'{nove_digitos}{digito1}{digito2}'

if cpf == cpf_calculo:
    print('O CPF é válido')
else:
    print('O CPF é inválido')