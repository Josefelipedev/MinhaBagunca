"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as classes que criam classes.
type é um metaclasse

"""

class Meta(type):
    def __new__(mcs, name , bases,namespace):
        if name =='A':
            return type.__new__(mcs,name,bases,namespace)

        if 'attr_classe' in namespace:
            del namespace['attr_classe']

        # if 'b_fala' not in namespace:
        #     print(f'Oi, você precisa criar o método b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um método e não um atributo{name}')

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'

class C(B):
    attr_classe = 'Valor C'


c = C()
print(c.attr_classe)

#criar classes usando type
class Pai:
    nome= 'Teste'

A = type('A', (Pai,),{'attr': 'Olá Mundo!'})

a= A()
print(a.nome)