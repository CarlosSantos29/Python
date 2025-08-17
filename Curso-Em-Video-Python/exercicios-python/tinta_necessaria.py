#7.Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m**2.
largura = float(input('Digite a lagura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros:'))
area = largura * altura
tinta_necessaria = area / 2
print(f'A area da parede é de {area:.2f}m e a quantidade de tinta necessaria para pinta-la é de {tinta_necessaria:.2f}litros.')
