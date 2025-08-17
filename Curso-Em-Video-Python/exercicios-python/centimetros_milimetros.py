#4. Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

numero = float(input('Digite um valor em metros: '))

km = numero / 10
hm = numero / 100
dam = numero / 1000
dm = numero * 10
cm = numero * 100
mm = numero * 1000

print(f'O valor de {numero}m corresponde a: \nKilometros: {km:.3f}km\nHectometros: {hm:.2f}hm\nDecametros: (dam:.2f)\nDecimetros: {dm:.2f}dm\nCentimetros: {cm:.2f}cm\nMilimetros: {mm:.2f}mm')
#print(f'O valor de {numero}m corresponde a: \nCentimetros: {numero * 100:.2f}cm\nMilimetros: {numero * 1000:.2f}mm')

