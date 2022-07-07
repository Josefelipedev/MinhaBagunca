import  sys
import time
# lista = list(range(10))
# print(lista)
# print(sys.getsizeof(lista))
#
# def gera():
#     for n in range(10):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
# print(next(g))
# print(g)
# for v in g:
#     print(v)

# lista = iter(lista)
# print(hasattr(lista,'__iter__'))
# for v in lista:
#     print(v)
# print(hasattr(lista,'__next__'))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))

# def gera():
#     variavel = 'Valor1'
#     yield variavel
#     variavel = 'Valor2'
#     yield variavel
#     variavel = 'Valor3'
#     yield variavel
#
#
# g = gera()
# for v in g:
#     print(v)
#
# print(next(g))
# print(next(g))
# print(next(g))

lista = list(range(1000))
lista = [x for x in range(1000)]
print(type(lista))
lista2 = (x for v in range(1000))

print(type(lista2))

print(sys.getsizeof(lista))
print(sys.getsizeof(lista2))
for  v in lista2:
    print(v)

