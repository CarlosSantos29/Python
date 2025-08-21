'''
3. Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.
(variavel % 2 == 0)
'''
numero =int(input('Digite um numero: '))

print('Calculando...')
if numero % 2 == 0:
    print(f'O numero solicitado: {numero}')
    print('è um numero par.')
else:
    print(f'O numero solicitado: {numero}')
    print('É um numero impar.')
print('-'*5+'Fim do código...')