# O uso de modulos em python
# import math
# import datetime
from random import random, randint
from math import sqrt, ceil
numero = int(input('Digite um numero: '))
raiz_quadrada = sqrt(numero)
print(f'A raiz quadrada de {numero} é igual a {ceil(raiz_quadrada)}')
# dia_atual = datetime.date.today() -- O dia atual
# dia_atual = datetime.datetime.now() -- o dia e a data atual
# print(f'Hoje é {dia_atual}')

numero = random()  # valor aleatorio
numero_2 = randint(1, 10)  # valor inteiro
print(f'numero gerado: {numero}')
print(f'Valor inteiro gerado: {numero_2}')

'''
    -------Exercicios 
    
    1. Crie um programa que leia um numero qualquer
    pelo teclado e mostre sua porção inteira.
    ex: Digite um numero: 6.127
    O numero 6.127 tem a parte inteira 6.
    
    2. Faça um programa que leia o comprimento
    do cateto oposto e do cateto adjacente de um
    triangulo retangulo, calcule e mostre o 
    comprimento da hipotenusa.
    
    3. Faça um programa que leia um angulo qualquer
    e mostre na tela o valor do seno, cosseno e
    tangente desse angulo.
    
    4. Um professor quer sortear um dos seus
    quatro alunos para apagar o quadro. Faça
    um programa que ajude ele, lendo o nome deles e
    escrevendo o nome do escolhido.
    
    5. O mesmo professor do desafio anterior quer
    sortear a ordem de apresentação de trabalhos dos
    alunos. Faça um programa, que leia o nome dos quatro
    alunos e mostre a ordem sorteada.
    
    6. Faça um programa em Python que abra e reproduza
    o audio de um arquivo mp3.
'''
