from  dados import produtos,pessoas,lista
def aumanta_preco(p):
    p['nova_idade'] = round(p['Idade'] * 1.20,3)
    return p

# nomes = map(lambda p: round(p['Idade']* 1.20,2), pessoas)
nomes = map(aumanta_preco, pessoas)

for pessoa in nomes:
    print(pessoa)





# def aumanta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05,2)
#     return p

# # precos = map(lambda p: p['preco'], produtos)
# precos = map(aumanta_preco , produtos)

# for preco in precos:
#     print(preco)


# for produto in produtos:
#     print(produto)


# nova_lista = map(lambda x: x*2, lista)
# nova_lista = [x*2 for x in lista]
# print(list(nova_lista))
# print(nova_lista)
# print(lista)


# for valor in nova_lista:
#     print(valor)