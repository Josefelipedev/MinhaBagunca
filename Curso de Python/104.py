"""
public, protected, private
_  --> recomenda que não acessa esse atributo. private mas fraca "protected"/public
__ --> privado,você não vai conseguir acessar esse atributo(__NOMECLASSE__nomeatributo)
um recomenda para não mexer dois você não vai.
"""

class BaseDeDados:
    def __init__(self):
        self.__dados= {}

    @property
    def dados(self):
        return  self.__dados

    def inserir_cliente(self,id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1,'João')
bd.inserir_cliente(2,'Tiago')
bd.inserir_cliente(3,'Rose')
bd.dados = ' Outro valor'
print(bd.dados)

# bd.__dados = 'Um novo valor'
# print(bd.__dados)
# print(bd._BaseDeDados__dados)