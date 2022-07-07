class A:
    vc = 123

    def __init__(self):
        # self.vc = 321
        pass



a1 = A()
a2 = A()

A.vc = 'Alterado'
# a1.vc = 321
#
# print(a1.__dict__)
# print(a2.__dict__)
# print(A.__dict__)

print()

print(a1.vc)
print(a2.vc)
print(A.vc)