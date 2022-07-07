# def is_float(val):
#     if isinstance(val, float): return True
#     if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_int(val):
#     if isinstance(val, int): return True
#     if re.search(r'^\-{,1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_number(val):
#     return is_int(val) or is_float(val)

#
# num = input('Digite um número:')
#
# if not num.isdigit():
#     print('Tem que ser um número :)')
#
# else:
#     num =int(num)
#     if num %2 ==0:
#         print('Ele é par.')
#     else:
#         print('Ele e impár:')

# hora = input('Que horas são:')
#
#
# x = 0
#
# while x < 3:
#
#     if not hora.isdigit():
#         print('Digite as horas em numeros.')
#         print(type(hora))
#     hora = int(hora)
#
#     if hora >= 0 and hora <= 11:
#         print('BOM DIA')
#         break
#
#     elif hora >= 12 and hora <= 17:
#         print('BOA TARDE :)')
#         break
#     elif hora >= 18 and hora <= 23:
#         print('BOA NOITE :)')
#         break
#     else:
#         print('Digitou um hora invalida:')
#         break


# nome = input('Digite o seu nome:')
#
# contador = len(nome)
#
# if contador <= 4:
#     print('Seu nome  curto.')
# elif contador >= 5 and contador <= 6:
#     print('Seu nome é normal.')
# elif contador >= 6:
#     print('Seu nome  muito grande.')
