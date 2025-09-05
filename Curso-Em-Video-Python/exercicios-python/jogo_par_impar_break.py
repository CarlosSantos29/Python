'''
3.Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou
no final do jogo.
'''

from random import randint

verificação = 'S'
jogador = lista = maquina = 0
while verificação in 'Ss':
    jogador = int(input('Vamos jogar par ou impar com a maquina, escolha um valor: '))
    lista = [jogador]
    maquina = randint(lista)
    verificação = str(input('Deseja continuar?(sim/não): '))

print(f'escolha da maquina:{lista}\nEscolha do jogador: {jogador}')