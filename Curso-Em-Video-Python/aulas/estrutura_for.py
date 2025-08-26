#Ainda será utilizado
'''for contador in range(0,6):
    print('Oi')
print('Fim')'''


for contador in range(6,0,-1):# do 6 até 0
    print(contador)
print('Fim')

for contador in range(0, 7):# do 0 até 6
    print(contador)
print('Fim')

for contador in range(0, 7, 2): #pulando 2 vezes de 0 até 6, evitando o 7
    print(contador)
print('Fim')

numero = int(input('Digite um numero: '))

# o usuario escolhe escolhe um numero e o contador irá de 0 ao numero solicitado adicionando +1
for contador in range(0, numero+1):
    print(contador)
    
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

#O usuario adiciona um valor para inicio e o fim do programa, e o passo representá o pulo.
for contador in range(inicio, fim + 1, passo):
    print(contador)
    

for contador in range(0, 3):
    numero = int(input('Digite um valor: '))


soma = 0
for contador in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero
print(f'O somatorio de todos os valores foi {soma}')

'''
exercicios For

1.Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles. (feito)

2. Faça um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50. (feito)

3.Faça um programa que calcule a soma entre os numeros impares que sao multiplos de três e que
se encontram no intervalo de 1 até 500. (feito)

4.Refaça o desafio 9, mostrando a tabuada de um numero que o usuario escolher, só que agora 
utilizando um laço for. (feito)

5.Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem
pares se o valor digitado for impar desconsidere. (feito)

6.Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10
primeiros termos dessa progressão.(feito)

7. Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.(feito)

8. crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
os espaços. ex: Apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo,
anotaram a data da maratona. (feito)

9.Crie um programa que leia o ano de nascimento de sete pessoa. No final, mostre quantas
pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.(maioridade 21 anos)(feito)

10. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor 
peso lidos.(feito)

11. Deenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-A media de idade do grupo.
-Qual o nome do homem mais velho
-Quantas mulheres tem menos de 20 anos.(feito)
 
'''