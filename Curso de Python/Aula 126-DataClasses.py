"""
126-DataClasses → o que são dataclasses ?
O módulo dataclasses fornece um decorador e
funções para criar automaticamente métodos,
 como __int___(), __repr__(),__eq__() (etc) em classes definidas pelo usuário.
 Basicamente dataclasses são syntax sugar para criar classes normais
, for originalmente descrito na PEP 557,Versão Python 3.7.
"""

from dataclasses import  dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(eq=True, repr=True, order=True,frozen=True,init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)


    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(f' Tipo inválido{type(self.nome).__name__}!= str em {self}')


    # @property
    # def nome_completo(self):
    #     return  f'{self.nome}{self.sobrenome}'

p1 = Pessoa('A', '1')
p2 = Pessoa('B', '2')
p3 = Pessoa('C', '3')
p4 = Pessoa('D', '4')
p5 = Pessoa('E', '5')
p6 = Pessoa('F', '6')

pessoas =[p1,p2,p3,p4,p5,p6]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse= True))
print(p1)

# print(p1)
# print(p2 == p1)
# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo())

print()
print(asdict(p1))
print(astuple(p1))
