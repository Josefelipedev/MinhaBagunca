from clientes import *

class ContaCorrente(Client):
    def __init__(self,nome,agencia,conta,saldo,limite,banco):
        super().__init__(nome,agencia,conta,saldo, banco)
        self._limite = limite


    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if(self._saldo + self._limite) < valor:
            print('Sem saldo para sacar')

        else:

            self._saldo -= valor
            self.detalhes()