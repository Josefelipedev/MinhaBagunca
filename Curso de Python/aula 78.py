from itertools import groupby,tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'José', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'E'},
    {'nome': 'Letícia', 'nota': 'C'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Tiago', 'nota': 'F'},
    {'nome': 'Luiz Gustavo', 'nota': 'B'},
    {'nome': 'Rose', 'nota': 'B'},
    {'nome': 'Rose', 'nota': 'B'},
    {'nome': 'Rose', 'nota': 'B'},
    {'nome': 'Rose', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'André', 'nota': 'C'},

]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados =groupby(alunos, ordena)
# alunos.sort(key=lambda  item:item['nota'])
# alunos_agrupados= groupby(alunos, lambda  item:item['nota'])
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento:{agrupamento}')
    for alunos in va1:
        print(f'\t {alunos}')
    quantidade= len(list(va2))
    print(f'{quantidade} alunos tiraram nota {agrupamento}')
    print()


