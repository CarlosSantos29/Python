'''
3. Crie um programa que leia o nome de uma 
cidade e diga se ela começa ou não com o nome
'SANTO'.
'''

nome_cidade = input('Digite uma cidade: ').upper().strip()
print(f'Essa cidade possui SANTO no nome: {nome_cidade.startswith('SANTO')}')