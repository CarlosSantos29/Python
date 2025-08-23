'''
 3. 
Escreva um programa que leia dois numeros inteiros e compare os, mostrando na tela
uma mensagem: O primeiro valor é maior, o segundo é maior, não existe valor maior,
os dois são iguais.


text                    background
 
30      black       preto          40
31      red           vermelho   41
32      green       verde         42
33      yellow      amarelo    43
34      blue          azul           44
35      Magenta  Magenta  45
36      cyan         ciano         46
37      grey          cinza         47
97      white        branco     107


style = 0(default) 1(negrito) 4(sublinhado) 7(inverte a cor)


cores = {'limpa':'\033[m',
         'vermelho':'\033[31m', 
         'azul-claro':'\033[93m',
         'verde-claro':'\033[92m',
         'inverte-cor':'\033[;7m',
         'black-red':'\033[7;30;41m',
         'cyan-green':'\033[4;36;42m'
         }

'''
from time import sleep

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

sleep(3)

if numero_1 > numero_2:
    maior_numero = numero_1
    print(f'O maior numero é {numero_1}')
elif numero_2 > numero_1:
    maior_numero = numero_2
    print(f'O maior numero é {numero_2} ')
elif numero_1 == numero_2:
    print('Ambos os numeros solicitados são iguais.')

