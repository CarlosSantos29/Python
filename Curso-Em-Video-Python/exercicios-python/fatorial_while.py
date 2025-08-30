'''4. Faça um programa que leia um numero qualquer e mostre seu fatorial
ex: 5! = 5x4x3x2x1 = 120
'''

from math import factorial
numero = int(input('Digite um valor, e veja sua fatorial: '))
contador = numero
#fatorial = 1
print(f'{numero}! = ',end =' ')

while contador > 0:
    print(f'{contador}', end=' ')
    print('x' if contador > 1 else '=', end=' ')
    #fatorial *= contador
    contador -= 1
#print(f'{fatorial}', end=' ')
print(f'{factorial(numero)}')