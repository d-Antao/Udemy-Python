
perguntas =[{
    'Pergunta':'quanto é 2+2 ?',
    'opções' : ['2','5','3','4'],
    'resposta' : '4'
},{
    'Pergunta':'quanto é 3*2?',
    'opções' : ['5','8','6','9'],
    'resposta' : '6'
},{
    'Pergunta':'quanto é 4/2?',
    'opções' : ['2','4','6','1.5'],
    'resposta' : '2'
}
]

while True:
    qtd_acertos =0
    
    for pergunta in perguntas:
        print(f'pergunta : {pergunta['Pergunta']}')
        print('as opções são :')
        print()
        
        opcoes = pergunta['opções']
        for i,opção in enumerate(opcoes):
            print(f'{i+1}) {opção}')
        print()
        resposta_usuario = input('sua resposta:')
        print()
        
        resposta_int = None
        qtd_opcoes = len(opcoes)
        

        if resposta_usuario.isdigit():
            resposta_int = int(resposta_usuario)
        print(opcoes[resposta_int-1])
        if resposta_int is not None:
            if resposta_int>=1 and resposta_int <= qtd_opcoes:
                if opcoes[resposta_int-1] == pergunta['resposta']:
                    qtd_acertos +=1
                    print('você acertou')
                else:
                    print('você errou')
            else:
                print('Errou')
                print('digite apenas digitos interios conpreendidos entre 1 a 4')
            print()
        else:
            print('errou')
            print('digite apenas digitos interios conpreendidos entre 1 a 4')
          
    print(f'Acertaste {qtd_acertos} em {len(perguntas)} perguntas')    
             
    resposta = input('você deseja continuar? [s/n]')
    if resposta == 'n':
        break