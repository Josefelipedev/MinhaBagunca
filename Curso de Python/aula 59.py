# def func(arg,agr2):
#     return arg * agr2
# var = func(2,2)
# print(var)
# a = lambda x, y: x * y
# print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 1],
    ['P3', 3],
    ['P4', 50],
    ['P5', 8],
]
# def func(item):
#     return  item[1]
# lista.sort(key=lambda  item: item[1], reverse=False)

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)
# lambda e um função(def) anônima que pode ser usada para passar parâmetros