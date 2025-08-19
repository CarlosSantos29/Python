'''
4. Um professor quer sortear um dos seus
quatro alunos para apagar o quadro. Faça
um programa que ajude ele, lendo o nome deles e
escrevendo o nome do escolhido.
'''

from random import choice

aluno_1 = input('Digite o primeiro aluno: ')
aluno_2 = input('Digite o segundo aluno: ')
aluno_3 = input('Digite o terceiro aluno: ')
aluno_4 = input('Digite o quarto aluno: ')

lista_sorteio = [aluno_1, aluno_2, aluno_3, aluno_4]
escolha_sorteio = choice(lista_sorteio)

print(f'O aluno escolhido foi {escolha_sorteio}')
