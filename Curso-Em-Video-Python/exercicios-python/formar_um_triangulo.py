'''
8. Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas
podem ou não formar um triangulo. A+B>C e A+C>B e B+C>A
'''

lado_1 = int(input('Digite o primeiro lado: '))
lado_2 = int(input('Digite o segundo lado: '))
lado_3 = int(input('Digite o terceiro lado: '))

print('Calculando...')
if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    triangulo = True
else:
    triangulo = False
print(f'L1: {lado_1}\nL2: {lado_2}\nL3: {lado_3}')
print(f'De acordo com os dados obtidos, pode formar um triangulo? {triangulo}')
print('-'*5+' Fim do codigo....')