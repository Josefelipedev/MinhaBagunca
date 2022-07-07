from dados import produtos,pessoas,lista

# nova_lista = filter(lambda x:x > 5,lista)
# nova_lista = [x for x in lista if x > 5]
# print(nova_lista)
# print(list(nova_lista))
# def filtra(produto):
#     if produto['preco'] > 10:
#         produto['e_caro'] = True
#         return True


# nova_lista = filter(lambda p:p['preco'] > 10 , produtos)
# nova_lista = filter(filtra,produtos)
#
# for produto in nova_lista:
#     print(produto)

def maior_idade(pessoas):
    if pessoas['Idade'] > 18:
        pessoas['Ele e maior'] = True
        return True
nova_lista = filter(maior_idade, pessoas)
for pessoas in nova_lista:
    print(pessoas)
