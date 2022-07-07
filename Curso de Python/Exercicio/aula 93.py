"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
from cnpjfunc import remover_carater

cnpj = '04.252.011/0001-10'
novo_cnpj = remover_carater(cnpj)
cnpj = novo_cnpj
total = 0
contagem_reversa = 0



for index in range(19):
    if index > 5:
        index -= 8


    total+= int(novo_cnpj[index]) * contagem_reversa
    contagem_reversa -=1

    if contagem_reversa < 2:
        contagem_reversa = 11
        d = 11 -(total % 11)

    if d > 9:
        d = 0
        total = 0
        novo_cnpj += str(d)


    sequencia = novo_cnpj == str(novo_cnpj[0]) * len(cnpj)

novo_cnpj = novo_cnpj[:-1]

if novo_cnpj == cnpj:
    print('Valido')
else:
    print('Invalido')
