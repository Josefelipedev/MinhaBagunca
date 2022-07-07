perguntas = {
    'Pergunta 1':{
    'Pergunta':'Qual o estado que você morar',
    'Respostas': {'a':'Santa Catarina','b':'São Paula',
     'c':'Goiânia',},
    'resposta_certa': 'a',
    },
    'Pergunta 2':{
    'Pergunta':'Quando você vai para o canadá',
    'Respostas': {'a':'2025','b':'2024',
     'c':'2023',},
    'resposta_certa': 'c',
    },
}
print()
respostas_certas = 0
for chave_p, chave_r in perguntas.items():
    print(f'{chave_p} : {chave_r["Pergunta"]}')
    print('Respostas:')

    for rk, rv in chave_r['Respostas'].items():
        print(f'[{rk}]:{rv}')
    resposta_usuario = input('Qual a sua respota?')
    print()
    if resposta_usuario == chave_r['resposta_certa']:
        print('CERTOU')
        respostas_certas += 1
    else:
        print('VOCE ERROU')

quantidade = len(perguntas)
porcentagem_acerto =  respostas_certas / quantidade * 100
print(f'Você acertou {respostas_certas} resposta.')
print(f'Acertou em porcentagem{porcentagem_acerto}%')
