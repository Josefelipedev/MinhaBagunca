# Lista,tuples, str __>Sequences -->iterável
nome = 'Jose Felipe'
itarador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('Olha o FOR')
for letra in gerador:
    print(letra)
print('Olha outro FOR')
for letra in gerador:
    print(letra)
print()
print('Não tem valor')

# try:
#     print(next(itarador))
#     print(next(itarador))
#     # print(next(itarador))
#     # print(next(itarador))
#     # print(next(itarador))
#     # print(next(itarador))
#
# except:
#     pass
# print(itarador)
# for n in itarador:
#     print(n)












# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)