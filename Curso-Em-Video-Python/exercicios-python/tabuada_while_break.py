'''2.Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para
cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado
for negativo.
'''
from time import sleep
numero = multiplicação = contador = 0
while True:
    numero = int(input('Digite um valor, e veja sua tabuada: '))
    if numero < 0:
            print('Saindo do codigo....')
            sleep(2)
            break
    else:
        for multiplicação in range(1, 11):
            print(f'{numero} x {multiplicação:2} = {numero * multiplicação}')
print('Fim....')
