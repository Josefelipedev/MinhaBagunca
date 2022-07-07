class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade , estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self,cidade,estado):
        self.estado = estado
        self.cidade = cidade

    def __del__(self):
        print(f'{self.cidade}/ {self.estado} FOI APAGADO')