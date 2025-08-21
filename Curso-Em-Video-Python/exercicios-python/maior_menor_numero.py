'''
6.Faça um programa que leia 3 numeros, e mostre 
qual é o maior e qual é o menor.
calculo -> para descobrir o maior =  A > B e A > C,
senão B > A e B > C (if if else)
'''

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_3 = int(input('Digite o terceiro numero '))

#maior numero

if numero_1 >= numero_2 and numero_1 >= numero_3:
    maior_numero = numero_1
else:
    if numero_2 >= numero_1 and numero_2 >= numero_3:
        maior_numero = numero_2
    else:
        maior_numero = numero_3

#Menor numero

if numero_1 <= numero_2 and numero_1 <= numero_3:
    menor_numero = numero_1
else:
    if numero_2 <= numero_1 and numero_2 <= numero_3:
        menor_numero = numero_2
    else:
        menor_numero = numero_3


#Resultado entre os três numeros
print(f'O maior numero: {maior_numero}')
print(f'O menor numero: {menor_numero}')
