# def fala_oi():
#     print('OI')
# variavel = fala_oi
#
# print(type(variavel))
#
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Eai gostoso')
#         funcao(*args,**kwargs)
#     return slave
#
# @master
# def fala_oi():
#     print('OI')
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
# outra_funcao('Outra mensagens')
# # fala_oi= master(fala_oi)
from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado=funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time-start_time)*1000
        print(f' \n A função {funcao.__name__} levou {tempo:.2f} ms para executar.')
        return resultado
    return interna
@velocidade
def demora():
    for i in range(1000):
        print(i,end='')
        # sleep(1)

demora()