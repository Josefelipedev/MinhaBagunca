# file = open('abc.txt', 'w+')
# file.write('Linha1\n')
# file.write('Linha2\n')
# file.write('Linha3\n')
#
#
# file.seek(0, 0)
# print('Lendo linhas:')
# print(file.read())
# print('###########')
#
# file.seek(0,0)
# print(file.readline(), end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print('###############')
#
# file.seek(0,0)
# for linha in file.readlines():
#     print(linha, end='')
#
# file.close()

# try:
#     file = open('abc.txt','w+')
#     file.write('linha')
#     file.seek(0,0)
#     print(file.read())
# finally:
#     file.close()

#
# with open('abc.txt','w+')as file:
#     file.write('linha 1\n')
#     file.write('linha 2\n')
#     file.write('linha 3\n')
#
#     file.seek(0)
#     print(file.read())

# with open('abc.txt', 'w+')as file:
#     file.write('Outra linha')
#     file.seek(0)
#     print(file.read())
# import os
# os.remove('abc.txt')

import json
d1 ={
    'Pessoa 1':{
        'nome':'luiz',
        'idade':25,
    },
    'Pessoa 2':{
        'nome':'Anna',
        'idade':24,
    }
}
d1_josn =json.dumps(d1, indent=True)

with open('abc.json','w+') as file:
    file.write(d1_josn)