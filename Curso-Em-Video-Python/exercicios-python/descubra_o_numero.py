'''
1.escreva uma programa que faça o computador pensar em um numero inteiro
entre o 0 e 5, e peça para o usuario tentar descobrir qual foi o numero escolhido
pelo computador.
o programa deverá escrever na tela se o usuario venceu ou perdeu.



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



'''
from random import randint
from time import sleep

print('=#='*20)
numero = int(input('Tente descobrir o numero entre 0 a 5\nAguardando sua resposta: '))
print('=#='*20)
cores = {'limpa':'\033[m',
         'magenta':'\033[45m'}
descobrindo_numero = randint(0, 5)

print('Gerando o numero...')
sleep(2)
if numero == descobrindo_numero:
    print(f'Seu numero: {numero}')
    print(f'O numero da máquina: {descobrindo_numero}')
    print('Parabens! você adivinhou o numero da maquina.')
else:
    print(f'Seu numero: {numero}')
    print(f'O numero da máquina: {descobrindo_numero}')
    print('Que pena! tente novamente.')
print('-'*5 + f'{cores["magenta"]}Fim...{cores['limpa']}')
