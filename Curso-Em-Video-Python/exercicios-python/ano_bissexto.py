'''
5.Faça um programa que leia o ano qualquer e mostre se ele é bissexto.
variavel bissexto / 4 e / 400.
'''
ano = int(input('Digite o ano desejado: '))

print('Calculando...')
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano é {ano}')
    print('ele é bissexto.')
else:
    print(f'O ano é {ano}')
    print('ele não é bissexto.')
print('----- Fim do código...')