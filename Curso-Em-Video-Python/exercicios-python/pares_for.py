'''5.Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem
pares se o valor digitado for impar desconsidere.'''
soma = 0
cont = 0
for numero_contador in range(1,7):
    numero = int(input(f'Escolha o {numero_contador} numero:'))
    
    if numero % 2 == 0:
        soma += numero
        cont += 1
    else:
        print(f'Esse numero: {numero} é impar, e não será calculado.')

print(f'Você informou {cont} numeros , e soma total dos numeros pares: {soma}')