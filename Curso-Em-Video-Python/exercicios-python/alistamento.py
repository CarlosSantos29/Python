'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade:
- se ele ainda vai se alistar ao serviço.
- se é a hora de se alistar.
- se ja passou do tempo do alistamento.

seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''


genero = str(input('Você é homem ou mulher?')).title()

if (genero == 'Mulher'):
    print('Você não precisa se alistar.')
else:
    from datetime import date
    ano_atual = date.today().year
    nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = ano_atual - nascimento
    print(f'Idade atual: {idade}')

    if idade < 18:
        diferenca_idade = 18 - idade
        saldo = ano_atual + diferenca_idade
        print('Você ainda não pode se alistar no exercito.')
        print(f'Faltam {diferenca_idade} anos para o alistamento.')
        print(f'Seu alistamento será em {saldo}')
    elif idade == 18:
        print('Já está na hora de você se alistar no exercito.')
    elif idade > 18:
        print('Já passou da hora de você se alistar, se informe direito.')
        diferenca_idade = idade - 18
        saldo = ano_atual - diferenca_idade
        print(f'Já passaram {diferenca_idade} anos do período de alistamento.')
        print(f'Seu alistamento foi realizado em {saldo}')
