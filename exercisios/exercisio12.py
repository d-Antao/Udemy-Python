
cpf = input('Digite seu CPF: ')
cpf_alt = cpf.replace('.', '').replace('-', '').replace(' ', '').replace(',', '').replace('_', '')
nove_digitos = cpf_alt[:9]
cont_reverse_1= 10
resultado_1 = 0
resultado_2 = 0
try:
    for digito in nove_digitos:
        resultado_1 += int(digito) * cont_reverse_1
        cont_reverse_1 -= 1
    digito_1 = resultado_1 * 10 % 11
    digito_1 = digito_1 if digito_1<= 9 else 0
    cont_reverse_1 = 11
    nove_digitos += str(digito_1)
    for digito in nove_digitos:
        resultado_2 += int(digito) * cont_reverse_1
        cont_reverse_1 -= 1
    digito_2 = resultado_2 * 10 % 11
    digito_2 = digito_2 if digito_2<= 9 else 0
    if cpf_alt == nove_digitos + str(digito_2):
        print('CPF válido')
    else:
        print('CPF inválido')
except ValueError:
    print('CPF inválido')
    
print(f'O valor do CPF {cpf} e {cpf_alt} é {digito_1} e o {digito_2}')