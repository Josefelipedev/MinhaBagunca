from  functools import reduce
from dados import  pessoas,produtos,lista


soma_idade = reduce(lambda ac,i: i['Idade']+ ac ,pessoas,0)
print(round(soma_idade/len(pessoas)))
# soma_precos = reduce(lambda ac, p: p['preco']+ ac,produtos, 0)
# print(soma_precos/len(produtos))


# soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
# print(soma_lista)

# acumula = 0
# for item in lista:
#     acumula += item
# print(acumula)