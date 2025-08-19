''' 
1. Crie um programa que leia um numero qualquer
pelo teclado e mostre sua porção inteira.
ex: Digite um numero: 6.127
O numero 6.127 tem a parte inteira 6.
'''
from math import trunc

numero = float(input('Digite um valor float: '))
# print(f'O numero solicitado: {numero}\nE sua porção inteira é {int(numero)}')
print(f'O numero solicitado: {numero}\nSua porção inteira: {trunc(numero)}')
