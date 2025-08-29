'''8. Crie um programa que leia varios numeros inteiros pelo teclado. O
programa só vai parar quando o usuario digitar o valor 999, que
é a condição de parada. No final mostre quantos numeros foram digitados
e qual foi a soma entre eles, desconsiderando o flag.
'''

contador = 0
soma = 0
numero = 0

while numero != 999:
    numero = int(input('Digite um valor: '))
    if numero != 999:
        contador += 1
        soma += numero
print(f'A quantidade de numeros digitados: {contador} e a soma entre eles é igual a {soma}')
