'''1. Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai
parar quando o usuario digitar o valor 999, que é a condição de parada. No final
mostre quantos numero foram digitados e qual foi a soma entre eles(desconsiderando o flag,)'''
from time import sleep
numero = contador = soma = 0

while True:
    numero = int(input('Digite um valor: '))
    if numero == 999:
        print('Saindo o codigo...')
        sleep(2)
        break
    contador += 1
    soma += numero

print(f'A quantidade de numeros solicitados pelo usuario foi {contador}, e sua soma é igual a {soma}.')