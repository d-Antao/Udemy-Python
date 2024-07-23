sair= True
while sair:
    
    numero1 = input('Insira um número: ')
    numero2= input('Insira outro número: ')
    operador = input('Insira um operador (+, -, *, /): ')
    
    try:
        num_f_1 = float(numero1)
        nume_f_2 = float(numero2)
    except:
        print('Valores inválidos, digite números')
        continue
    
    if operador not in ['+', '-', '*', '/'] or len(operador) > 1:
        print('Operador inválido')
        continue
    
    if operador == '+':
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
        
    elif operador == '-':
        print(f'{numero1} - {numero2} = {numero1 - numero2}')
        
    elif operador == '*':
        print(f'{numero1} * {numero2} = {numero1 * numero2}')
            
    elif operador == '/':
        print(f'{numero1} / {numero2} = {numero1 / numero2}')
    
        
    try:
        sair = str(input('Deseja sair? (s/n) '))
        if sair == 's':
            sair = False
        elif sair == 'n':
            sair = True
    except:
        print('pff digite s ou n para sair ou continuar!')