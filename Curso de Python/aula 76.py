"""
count - Itertools
"""

from  itertools import count
# contador = count(start=16, step=-1)

contador = count()
lista = ['jose', ' Maria','João']
lista = zip(contador,lista)
print(list(lista))

# for valor in contador:
#     print(round(valor, 2))
#
#     if valor >= 19 or valor <= -20:
#         break


# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
