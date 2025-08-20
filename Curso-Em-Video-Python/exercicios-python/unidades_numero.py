'''2. Faça um programa que leia 
um nnnnumero de 0 a 9999 e mostre
na tela cada um dos digitos separados.
ex: Digite um numero: 1834.
unidade: 4 Dezena: 3 Centena: 8 Milhar: 1
'''
'''numero = int(input('Digite um numero entre 0 a 9999: '))
#Resolvendo da primeira forma, sem manipular strings.
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'O numero solicitado: {numero}\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')'''

#Resolvendo de outra forma que seria manipulando com string, e o uso do zfill() que é para limitar a quantidade de numeros

numero = str(input('Digite um numero de 0 a 9999: ')).zfill(4)
lista = numero.split()
print(f'O numero solicitado: {numero}\nUnidade: {numero[3]}\nDezena: {numero[2]}\nCentena: {numero[1]}\nMilhar: {numero[0]}')