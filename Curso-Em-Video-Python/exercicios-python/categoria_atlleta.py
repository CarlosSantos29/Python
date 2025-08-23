'''
6. A confederação Nacional de Natação precisa de um prorgrama que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infatil
- Até 19 anos: Junior
- Até 20 anos: Senior
- Acima: Master
'''
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade_atual = ano_atual - ano_nascimento

print(f'A idade atual do atleta: {idade_atual} anos.')

if idade_atual <= 9:
    print('Classificação: Mirim')
elif idade_atual <= 14:
    print('Classificação: Infantil')
elif idade_atual <= 19:
    print('Classificação: Junior')
elif idade_atual <= 20:
    print('Classificação: Senior')
else:
    print('Classificação: Master')
