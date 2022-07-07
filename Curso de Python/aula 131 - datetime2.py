from datetime import datetime
from locale import  setlocale,LC_ALL
from calendar import mdays

setlocale(LC_ALL,'') #pt_br.utf-8 --> vai falar que e no brasil

# Sexta, 13 de junho de 2019

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(mes_atual,mdays[mes_atual])
print(formatacao)
print(formatacao2)