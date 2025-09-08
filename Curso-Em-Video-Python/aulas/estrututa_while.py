'''Essa parte ainda será editada
aos poucos terá atualização.

for contador in range(1,11):
    print(f'{contador}', end=' ')

contador = 1 
while contador < 10:
    print(contador)
    contador += 

for contador in range(1, 5):
   # print(f'{contador}')
   numero = int(input(f'Digite o {contador} valor: '))

numero = 1

while numero != 0:
    numero = int(input('Digite um valor: '))

resposta = 'S'

while resposta == 'S':
    numero = int(input('Digite um valor: '))
    resposta = str(input('Deseja continuar? (Sim/Não): ')).upper()'''

numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} pares e {impar} impares.')

'''
exercicios

1. Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
até ter um valor correto.(feito)

2. Melhore o desafio 28 onde o computador vai pensar em um numero
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertr, 
mostrando no final quantos palpites foram necessarios para vencer.(feito)

3.Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa

seu programadeverá realizar a operação solicitada em cada caso.(feito)

4. Faça um programa que leia um numero qualquer e mostre seu fatorial
ex: 5! = 5x4x3x2x1 = 120 feito

5. Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressao usando a estrutura 
while. feito

6. Melhore o desafio 61 perguntando para o usuario se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer 
mostrar 0 termos. feito

7. Escreva um programa que leia um numero n inteiro quealquer e mostre
na tela os n primeiros elementos de uma sequencia de fibonnaci.
ex: 0 > 1 > 1 > 2 > 3 > 5 > 8 feito

8. Crie um programa que leia varios numeros inteiros pelo teclado. O
programa só vai parar quando o usuario digitar o valor 999, que
é a condição de parada. No final mostre quantos numeros foram digitados
e qual foi a soma entre eles, desconsiderando o flag.(feito)

9. Crie um programa que leia varios numeros inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qal foi o
maior e o menor valores lidos. O programa deve perguntar ao usuario
se ele quer ou não continuar a digitar valores.(feito)



'''