"""
Combinations, Permutations e product - itertools
combinação - ordem não importa
permutação - Ordem importa
ambos não repetem valores únicos
produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations,product

pessoa = ['Luiz', 'José', 'Eduardo','André'
          ,'Letíca','Fabríco','Rose']
for grupo in product(pessoa, repeat= 2):
    print(grupo)