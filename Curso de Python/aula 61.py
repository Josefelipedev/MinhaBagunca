# d1 = {'chave1': 'valor da chave'}
# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')

# d1 = {'chave' : 'valor','chave' : 'valor','chave' : 'valor','chave' : 'valor da real da chave'}
# para aparecer o valor das outra chave tem que mundar o nomes delas ou valor muitas pessoa usar isso
# d1['nova_chave'] = 'valor da nova chave'
# print(d1)

d1 = {
    'chave1' : 'Valor',
    'chave2': 'Outra valor',
    'chave3' : 'Tupla',

}
# d1['nãoexiste'] = ' Agora existe.'
# if 'nãoexiste'  in d1:
#     print( d1['nãoexiste'] )
# d1['str'] = 'José Felipe'
# d1.update({'nova_chave':'novo_valor'})
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
# print(123)
# del d1['str'] apagar valor
# print(d1)

# print('str' in d1)  ver se tem no dicionario
# print('valor' in d1.values()) essa função e olha se tem o valor
# print('str' in d1.keys()) esse função olha as chave
# print(len(d1)) len o a quantidade de pares

# for k, v in d1.items():   #items acessar os pares
    # print(k)
    # print((k[0]), k[1])
    # print(k, v)

# cleintes = {
#     'cliente1' : {
#       'nome' : 'luiz',
#         'sobrenome' : 'Otávio',
#     },
#     'cliente2': {
#         'nome': 'joão',
#         'sobrenome': 'Moreira',
#     }
# }
# for cleintes_k, cleintes_v in cleintes.items():
#     print(f'Exibindo {cleintes_k}')
#     for dados_k, dados_v in cleintes_v.items():
#         print(f'\t {dados_k}= {dados_v}')
import copy # com esse import voce consegue copia e altera sem mudar a principal
# d1 = {1: 'a', 2: 'b', 3: 'c', 'd' :['Jose','Felipe']}
# v = copy.deepcopy(d1) # isso e com copia do dicionario os valores são referencia
# v[1] = 'Luiz'
 #v[1] = 'Luiz' #a duas vão mudar o d1 e o V são iguais
# v['d'][0] = 'Joãozinho'
# print(d1)
# print(v)
#
# lista = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ]
# d1 = dict(lista)
# print(d1)
# print(d1['c3'])
d1 = {
    1: 2,
    2: 3,
    4: 5,
}
# d1.popitem() eliminar um item pop e popitem o ultimo item não importa qual
# print(d1)
d2 = {
    'a' : 'b',
    'c' : 'd',
}
print(d1)
print(d2)
d1.update(d2)
print(d1)
