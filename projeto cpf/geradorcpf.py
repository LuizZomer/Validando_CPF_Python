from random import randint 

nove_digitos = ''

for i in range(9):
    nove_digitos += str(randint(0,9))

cont = 10

soma_1 = 0

for numero in nove_digitos:
    soma_1 += int(numero) * cont    
    cont -=1

digito1 = (soma_1 * 10) % 11

digito1 = digito1 if digito1 <=9 else 0

dez_digitos = nove_digitos + str(digito1)

soma_2 = 0
cont_1 = 11

for numero in dez_digitos:
    soma_2 += int(numero) * cont_1
    cont_1 -= 1
digito2 = (soma_2 * 10) % 11

digito2 = digito2 if digito2 < 10 else 0

cpf_calculo = f'{nove_digitos}{digito1}{digito2}'
print(cpf_calculo)

