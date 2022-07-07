# Maneira para manipular arquivos.


# arquivos = open('abc.txt', 'w')
# arquivos.write('Alguma coisa')
# arquivos.close()
"""
class Arquivo:
    def __init__(self, arquivos, modo):
        print('Abrindo arquivos.')
        self.arquivos = open(arquivos, modo)

    def __enter__(self):
        print('Retornando arquivos')
        return self.arquivos

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivos.')
        self.arquivos.close()


# NO lugar do codigo a cima.
with open('abc.txt','w') as arquivo:
    arquivo.write('Alguma coisa')
"""
from  contextlib import  contextmanager

@contextmanager
def abrir(arquivo, modo ):
    try:
        print('Abrindo arquivo...')
        arquivo = open(arquivo,modo)

        yield arquivo
    finally:
        print('Fechando arquivo...')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write("LInha 1")
    arquivo.write("LInha 2")
    arquivo.write("LInha 3")