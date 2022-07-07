def mostrar(tarefas_totais):
    print()
    print('Tarefas:')
    print(tarefas_totais)
    print()




def remover(tarefas_totais, tarefas_remover):
    if not tarefas_totais:
        print('Nada a remover')
        print()
        return
    tarefas_recur = tarefas_totais.pop()
    tarefas_remover.append(tarefas_recur)
def defazer(tarefas_totais,tarefas_remover):
    if not tarefas_totais:
        print('Nada para defazer :)')
        print()
        return
    tarefas_recur = tarefas_totais.pop()
    tarefas_remover.append(tarefas_recur)






if __name__ == '__main__':
    tarefas_totais = []
    tarefas_remover = []

def para_lista(entrada,tarefas_totais):
    tarefas_totais.append(entrada)


while True:
    entrada = input('Digite um tarefa - remover,mostrar ,defazer:')


    if entrada == 'mostrar':
        mostrar(tarefas_totais)
        continue
    elif entrada == 'remover':
        remover(tarefas_totais,tarefas_remover)
        continue
    elif entrada == 'defazer':
        defazer(tarefas_totais,tarefas_remover)
        continue

    para_lista(entrada,tarefas_totais)

