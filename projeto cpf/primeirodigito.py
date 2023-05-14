cpf = '74682489070'

nove_digitos = cpf[:9]

cont = 10

soma_1 = 0

for numero in nove_digitos:
    soma_1 += int(numero) * cont    
    cont -=1

digito1 = (soma_1 * 10) % 11

print(digito1)

digito1 = 0 if digito1 > 10 else digito1

dez_digitos = cpf[:10]

soma_2 = 0
cont_1 = 11

for numero in dez_digitos:
    soma_2 += int(numero) * cont_1
    cont -= 1
digito2 = (soma_2 * 10) % 11

digito2 = 0 if digito2 > 10 else digito2

print(digito2)
