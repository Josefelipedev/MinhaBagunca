# lista = [
#     ('Chave','valor'),
#     ('Chave2','valor2'),
# ]

# d1 = {x: y.upper() for x, y in lista}
# d2 = dict(lista)
# print(d1)
# print(d2)

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))