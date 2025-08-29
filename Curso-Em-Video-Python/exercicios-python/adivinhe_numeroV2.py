'''2. Melhore o desafio 28 onde o computador vai pensar em um numero
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertr, 
mostrando no final quantos palpites foram necessarios para vencer.
'''
from random import randint

usuario = int(input('Tente adivinhar um numero de 0 a 10 que a maquina pensou.\nAqui vai sua resposta: '))
maquina = randint(0, 10)
tentativas = 1

while usuario != maquina:
    usuario = int(input('Tente novamente, pense em um numero de 0 a 10.\nAqui vai sua resposta: '))
    tentativas += 1
    if usuario == maquina:
        print(f'Parabens você conseguiu, foi necessario {tentativas} tentativas.')