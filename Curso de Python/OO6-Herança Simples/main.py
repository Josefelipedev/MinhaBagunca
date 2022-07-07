from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Cliente('José', 23)
print(c1.nome)
c1.falar()
c1.comprar()
a1 = Aluno('Felipe',25)
print(a1.nome)
a1.estudar()
a1.falar()