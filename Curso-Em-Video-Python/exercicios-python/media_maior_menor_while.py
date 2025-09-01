'''9. Crie um programa que leia varios numeros inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual foi o
maior e o menor valores lidos. O programa deve perguntar ao usuario
se ele quer ou não continuar a digitar valores.
'''

verificação = 'S'
contador = soma = media = maior = menor = 0

while verificação in 'Ss':
    numero = int(input('Digite um valor: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        
    verificação = str(input('Deseja continuar? (Sim/Não): ')).upper().strip()[0]
media = soma / contador
print(f'O usuario solicitou {contador} numeros, sua média é igual a {media}, o maior numero é {maior} e o menor numero é igual a {menor}.')