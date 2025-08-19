'''
5. O mesmo professor do desafio anterior quer
sortear a ordem de apresentação de trabalhos dos
alunos. Faça um programa, que leia o nome dos quatro
alunos e mostre a ordem sorteada.
'''
from random import shuffle

aluno_1 = input('Digite o primeiro aluno: ')
aluno_2 = input('Digite o segundo aluno: ')
aluno_3 = input('Digite o terceiro aluno: ')
aluno_4 = input('Digite o quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
ordem_apresentação = shuffle(lista_alunos)

print(f'A ordem gerada para apresentação: {lista_alunos}')
