'''
9.Crie um programa que leia o ano de nascimento de sete pessoa. No final, mostre quantas
pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.(maioridade 21 anos)'''
from datetime import date
data_atual = date.today().year

maioridade = 0
menoridade = 0

for contador in range(1, 8):
    data_nascimento = int(input(f'Digite a {contador} de nascimento: '))
    idade_atual = data_atual - data_nascimento
    
    if idade_atual <= 21:
        menoridade += 1
    elif idade_atual >= 21:
        maioridade += 1
        
    
print(f'O total de pessoas que não estão na maioridade: {menoridade}')
print(f'O total de pessoas que já está na classificação de maioridade: {maioridade}')