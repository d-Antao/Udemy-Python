# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls
#--------------------------------------------------------------------------------------
# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os

#os.system('clear')
#os.system('echo "Hello world"')

# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
# print(caminho)
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(nome_arquivo, extensao_arquivo)
# print(os.path.exists('/Users/luizotavio/Desktop/curso-python-rep'))
# print(os.path.abspath('.'))
print(caminho)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))