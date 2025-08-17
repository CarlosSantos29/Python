#2. Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um numero qualquer: '))

'''
dobro = numero * 2
triplo = numero * 3
raizQuadrada = pow(numero,(1/2))

print(f'O numero solicitado: {numero}\nSeu dobro: {dobro}\nSeu triplo: {triplo}\nSua raiz Quadra: {raizQuadrada:.2f}')
'''

print(f'O numero solicitado: {numero}\nSeu dobro: {numero * 2}\nSeu triplo: {numero * 3}\nSua raiz quadrada: {pow(numero, (1/2)):.1f}')
