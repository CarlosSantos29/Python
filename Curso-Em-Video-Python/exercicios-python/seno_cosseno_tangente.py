'''
3. Faça um programa que leia um angulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse angulo.
'''
from math import sin, cos, tan, radians

numero_angulo = float(input('Digite um numero: '))
numero_radiano = radians(numero_angulo)
print(f'O numero solicitado é {numero_angulo}\nSeu seno: {sin(numero_radiano):.2f}\nSeu Cosseno: {cos(numero_radiano):.2f}\nE sua tangente: {tan(numero_radiano):.2f}')
