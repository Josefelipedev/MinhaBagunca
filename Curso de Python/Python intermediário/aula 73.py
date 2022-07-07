"""
Zip - unindo iteráveis
Zip_longest - itertools
"""
### Códígo
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte','Salvador','Monte Belo','Goiãnia']

# Codígo
estados =['SP','MG','BA','GO']

cidades_estados = zip(indice,cidades, estados)  # inverter os nome mudar a ordem
#print(list(cidades_estados)) # posso usar dict

for indice,estados,cidades in cidades_estados: # ou for valor in cidades_estados
    print(indice,estados,cidades)