# Add(adiciona),update(atualiza), clear, discard(remover elementos)
# union| (une)
#intersection & (todos os elementos presentes nos dois sets)
#difference - (eleementos apenas no set da esquerda)
#symmetric_difference^(Elementos que estão nos dois sets, mas não em ambos)
#  set não aceita elementos duplicados
# s1 = {1,2,3,4,5,6}
#
# for v in s1:
#     print(v)

# s1  = set()
# s1.update('Python')
# s1.add(1)
# s1.add(2)
# s1.add((1,2,3,"Jose Felipe"))
# s1.discard(2)
# print(s1)
# s1 = {1,2,3,4,5,7}
# s2 = {1,2,3,4,5,6}
# s3 = s1 | s2 pegar todos e colacar em um só
# s3 = s1 & s2  pegar os menos
# s3 = s1 - s2 - o estrelinha o unico entrei eles mais de forma prioritaria
# s3 = s1 ^ s2 são unicos no dois elementos
# print(s3)

l1 = ['José ', 'João', 'Maria']
l2 = ['João','Maria','Maria','José','José','José','José','José','José']

l1 = set(l1)
l2 = set(l2)
print(l1)
print(l2)