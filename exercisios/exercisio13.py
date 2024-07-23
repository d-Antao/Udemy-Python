def multiplicaçao(*args):
    total = 1
    for numero in args:
        total *= numero  
    return total
    
def par_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f'O número {numero} é par')
        else:
            print(f'O número {numero} é ímpar')


print(f'a multiplicão dos {multiplicaçao(1,2,3,4,5,6)}')
par_impar(0,1,2,3,4,5,6)