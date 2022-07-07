from classes import *

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')


        self.saldo -= valor
        self.detalhes()