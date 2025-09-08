contador = 1
'''
while contador <= 10:
    print(contador, '', end='')
    contador += 1
print('Acabou.')
'''
palavra = 'acabou'
numero = soma = contador = 0
while True:
    numero = int(input('Digite um valor: '))
    '''contador += 1'''
    if numero == 999:
        break
    soma += numero
print(f'A soma equvale a {soma}')
print(f'{palavra:^20}')# centralizado.

'''
exercicios While com Break

1. Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai
parar quando o usuario digitar o valor 999, que é a condição de parada. No final
mostre quantos numero foram digitados e qual foi a soma entre eles(desconsiderando o flag,)(feito)

2.Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para
cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado
for negativo.(feito)

3.Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou
no final do jogo.

4. Crie um programa que leia o sexo de varias pessoas. Caa pessoa caastrada, o programa
deverá perguntar se o usuario quer ou não continuar, no final mostre:
a) quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tm menos de 20 anos.

5.Crie um programa que leia o nome e o preço e varios proutos. O programa deverá
perguntar se o usuario vai continuar. No final mostre:
a) Qual é o total gasto na compra.
B) Quantos proutos custam mais de R$1000
c) Qual é o nome o prouto mais barato.

6.Crie um programa que simule o funcionamento de um caixa eletronico, No inicio,
pergunte ao usuario qual será o valor a ser sacado(numero inteiro) e o programa
vai informar quantas cedulas de cada valor será entregue.
obs: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.

'''