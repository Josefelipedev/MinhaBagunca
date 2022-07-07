from clientes import Client

class ContaPoupanca(Client):
    def __init__(self,nome,agencia,conta,saldo,banco):
        super().__init__(nome,agencia,conta,saldo, banco)

    def sacar(self, valor):
        if self.saldo < valor:
            print('Voce não tem Limite.')

        else:
            self.saldo -= valor
