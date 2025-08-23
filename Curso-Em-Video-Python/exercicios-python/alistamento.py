'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade:
- se ele ainda vai se alistar ao serviço.
- se é a hora de se alistar.
- se ja passou do tempo do alistamento.

seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
ano_atual = date.today().year
# ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano do seu nasicmento: '))
idade = ano_atual - ano_nascimento
print(f'Idade atual: {idade}')

if idade < 18:
    diferenca_idade = 18 - idade
    print('Você ainda não pode se alistar no exercito.')
    print(f'Faltam {diferenca_idade} anos para o alistamento.')
elif idade == 18:
    print('Já está na hora de você se alistar no exercito.')
else:
    print('Já passou da hora de você se alistar, se informe direito.')
    diferenca_idade = idade - 18
    print(f'Já passaram {diferenca_idade} anos do período de alistamento.')
