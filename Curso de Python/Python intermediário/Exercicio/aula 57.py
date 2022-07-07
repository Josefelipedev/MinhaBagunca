"""
1-Crie uma função 1 que recebe um função2 como parÂmentro e retorne o valor
da função2 executada.

"""
# def ola_mundo():
#     return 'Olá mundo jose!'
#
# def mestre(funcao):
#     return funcao()
# executando = mestre(ola_mundo)
# print(executando)



"""
Crie um função1 que recebe uma função2 como parâmetro e retorne o valor da função2
executada.Faça a função1 executar duas funções que recebam um número
diferente de argumentos.

"""
def mestre(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)

def fala_oi(nome):
    return f'Oi{nome}'
def saudacao(nome, saudacao):
    return f'{saudacao}{nome}'

execuntando = mestre(fala_oi, "José")
execuntando2 = mestre(saudacao, " José", saudacao=" bom dia")
print(execuntando2)
print(execuntando)