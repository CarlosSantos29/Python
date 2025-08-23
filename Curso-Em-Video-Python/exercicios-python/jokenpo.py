'''
10. Crie um programa que faça o computador jogar Jokenpo com você.
Tesoura corta Papel
Papel cobre Pedra
Pedra esmaga Lagarto
Lagarto envenena Spock
Spock esmaga (ou derrete) Tesoura
Tesoura decapita Lagarto
Lagarto come Papel
Papel refuta (ou refuta) Spock
Spock vaporiza Pedra
Pedra quebra (ou amassa) Tesoura 


no momento farei o jokenpo tradicional pedra papel tesoura, mas pra frente irei refazer esse codigo.

Versão feita por mim:

from random import choice
print('-'*5+'Jokenpo'+'-'*5)
jogador = str(input('Escolha entre:\n\n1.Pedra\n2 Papel\n3.Tesoura\nO que deseja?')).title()
jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolha_maquina = choice(jokenpo)

print(f'Escolha do jogador: {jogador}')
print(f'Escolha da maquina: {escolha_maquina}')

if jogador not in jokenpo:
    print('Opção invalida, tente novamente.')
elif jogador in jokenpo:
    if jogador == escolha_maquina:
        print('Empate.')
elif jogador != escolha_maquina:
    if jogador == 'Pedra' and escolha_maquina == 'Papel':
        print('Perdeu!! tente novamente.')
    elif jogador == 'Papel' and escolha_maquina == 'Pedra':
        print('Parabens!! você ganhou.')
    elif jogador == 'Tesoura' and escolha_maquina == 'Papel':
        print('Parabens!! você ganhou.')
    elif jogador == 'Papel' and escolha_maquina == 'Tesoura':
        print('Perdeu!! tente novamente.')
    elif jogador == 'Pedra' and escolha_maquina == 'Tesoura':
        print('Parabens!! você ganhou.')
    elif jogador == 'Tesoura' and escolha_maquina == 'Pedra':
        print('Perdeu!! tente novamente.')



print('Fim do jogo.')
'''

'''essa outra desenvolvi porém mais reduzida, no codigo anterior também funciona entretanto notasse que é mais cheio e menos limpo que um codigo
normal de python na qual precisa seguir, lembrando que o de cima não está terminado, a logica funciona normalmente, mas iria precisar de alguns ajustes.'''

from random import choice
print('-'*5+'Jokenpo'+'-'*5)
#jogador = str(input('Escolha entre:\n\n1.Pedra\n2 Papel\n3.Tesoura\nO que deseja?')).title()
#jokenpo = ['Pedra', 'Papel', 'Tesoura']
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m', 
         'azul-claro':'\033[93m',
         'verde-claro':'\033[92m',
         'inverte-cor':'\033[;7m',
         'black-red':'\033[7;30;41m',
         'cyan-green':'\033[4;36;42m',
         'red-white':'\033[1;31;107m'}

print('=#='*5+f'{cores['azul-claro']}JOKENPO{cores['limpa']}'+'=#='*5)

jogador = int(input('Escolha entre:\n\n1.Pedra\n2 Papel\n3.Tesoura\nO que deseja?'))
regras = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
jokenpo = [1, 2, 3]
maquina = choice(jokenpo)

print(f'Escolha do jogador: {regras[jogador]}')
print(f'Escolha da maquina: {regras[maquina]}')

if jogador not in jokenpo:
    print('Opção Invalida, tente novamente.')
else:
    if jogador == maquina:
        print('Empate.')
    elif jogador == 2 and maquina == 1 or jogador == 3 and maquina == 2 or jogador == 1 and maquina == 3:
        print('Parabens!! você ganhou.')
    else:
        print('Perdeu!! tente novamente.')

print('Fim do jogo...')