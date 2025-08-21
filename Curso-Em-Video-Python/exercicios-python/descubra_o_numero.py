'''
1.escreva uma programa que faça o computador pensar em um numero inteiro
entre o 0 e 5, e peça para o usuario tentar descobrir qual foi o numero escolhido
pelo computador.
o programa deverá escrever na tela se o usuario venceu ou perdeu.
'''
from random import randint

numero = int(input('Tente descobrir o numero entre 0 a 5\n'))

descobrindo_numero = randint(0, 5)

print('Gerando o numero...')
if numero == descobrindo_numero:
    print(f'Seu numero: {numero}')
    print(f'O numero da máquina: {descobrindo_numero}')
    print('Parabens! você adivinhou o numero da maquina.')
else:
    print(f'Seu numero: {numero}')
    print(f'O numero da máquina: {descobrindo_numero}')
    print('Que pena! tente novamente.')
print('-'*5 + 'Fim...')
