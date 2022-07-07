#Setter = configurando um valor(=)
#Getter = obter um valor(.)

class Pessoa:


    def __init__(self, nome):
        self.nome = nome
    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, nome):
        print('Setter foi executado')
        nome += 'Sei La'
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Desconhecido'


p1 = Pessoa('José')
print(p1.nome)
print(p1.sobrenome)