try:
    a= 1/0
    # print(a[3])
except NameError as erro:
    print('Erro',erro)
except (IndexError,KeyError) as erro:
    print('Erro de Indice')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    # print('Seu código foi executado com sucesso')
    # print(a)
    pass
finally:
    a = None
    # print('Finalmente.')
# print(' Bora continuar')
print(a)
