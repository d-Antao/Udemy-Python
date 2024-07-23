primeiro_valor = input('digit um valor: ')
segundo_valor = input('digit outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}.')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor ({segundo_valor}) é maior que o primeiro ({primeiro_valor}).')
else:
    print(f'Os valores são iguais ({primeiro_valor} = {segundo_valor}).')