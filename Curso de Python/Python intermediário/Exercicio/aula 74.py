lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
lista_uni = []
lista_uni = [sum(x) for x in zip(lista_a,lista_b)]

print(lista_uni)

# for soma_valores in zip(lista_a,lista_b):  # in range(len(lista_b)):
#     print(sum(soma_valores)
#todas a linguagens
# for x in range(len(lista_b)): # posso usar o enumerate x,_
#     lista_uni.append(lista_a[x] + lista_b[x])
# print(lista_uni)

# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)  # Saída: [22, 4, 6, 10, 55]
#
# from itertools import zip_longest
#
# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
