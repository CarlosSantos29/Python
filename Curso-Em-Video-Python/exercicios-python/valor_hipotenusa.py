'''
2. Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente de um
triangulo retangulo, calcule e mostre o 
comprimento da hipotenusa.
'''
from math import hypot

cateto_oposto = int(input('Digite o cateto Oposto: '))
cateto_adjacente = int(input('Digite o cateto Adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O valor do cateto da hipotenusa vale: {hipotenusa:.2f}')
