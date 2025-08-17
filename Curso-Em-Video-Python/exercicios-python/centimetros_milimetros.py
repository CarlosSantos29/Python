#4. Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

numero = float(input('Digite um valor em metros: '))
'''
centimetros = numero * 100
milimetros = numero * 1000
print(f'O valor de {numero}m corresponde a: \ncentimetros: {centimetros:.2f}cm\nMilimetros: {milimetros:.2f}mm')
'''
print(f'O valor de {numero}m corresponde a: \nCentimetros: {numero * 100:.2f}cm\nMilimetros: {numero * 1000:.2f}mm')


