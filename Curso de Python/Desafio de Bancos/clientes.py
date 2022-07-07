from abc import abstractmethod


class Client():
    def __init__(self, nome, agencia, conta, saldo,banco):
        self._nome = nome
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self._banco = banco

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def nome(self):
        return self._nome

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Precisa sem numerico.')

        self._saldo = valor
        self.detalhes()

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Precisa sem numerico.')

        self._saldo += valor
        self.detalhes()

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Precisa sem numerico.')

        self._saldo -= valor
        self.detalhes()

    def detalhes(self):
        print(f'Nome do Cliente: {self.nome}', end=' ')
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}', end=' ')

    @abstractmethod
    def sacar(self, valor):
        pass

    @property
    def banco(self):
        return self._banco

    def checar(self):
        bancos = 'Inter'
        if  self._banco == bancos and self._agencia == self.agencia:
            print('Esse é seu banco...')

        else:
            print('Esse não é seu banco....')


