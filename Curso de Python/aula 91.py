#Objetos mudaveis(mutable) = lista dicionários e ....
#objetos inmudaveis=tuplas,strg,números,True, NONE, False

def lista_de_clientes(clientes_iteravel,lista=None):
    if lista is None:
        lista=[]
    lista.extend(clientes_iteravel)
    return lista
lista_de_clientes1 = ['Carla']
clientes1 = lista_de_clientes(['João','Maria','Eduardo'], lista_de_clientes1)
clientes2 = lista_de_clientes(['Zé','Luiz','Zico'])
clientes3 = lista_de_clientes(['Felipe'])

print(clientes1)
print(clientes2)
print(clientes3)

