import os

palavra_secreta = 'perfume'
letras_acertadas = ''
cont = 0   
while True:
    
    cont += 1
    letra = input('Digite uma letra: ')
        
    
    if letra == letra.isdigit():
        print('Você digitou um número!')
        continue
    if len(letra)!= 1:
        print('Você digitou nenhuma ou mais de uma letra!')
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    palavra_formatada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'
    else:
        print('voce errou a letra tente novamente!')
    print(palavra_formatada)
    
    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print(f'voce acertou a palavra!, em {cont} tentativas a palavra era {palavra_secreta}! parabéns')
        cont=0
        palavra_formatada = ''
        letras_acertadas = ''
    
    
    
        