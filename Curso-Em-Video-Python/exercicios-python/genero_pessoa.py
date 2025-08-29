'''1. Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
até ter um valor correto.'''

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'Qual seu genero? (M/F): ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção invalida.')
        sexo = str(input(f'Qual seu genero? (M/F): ')).upper()
    else:
        print('Saindo do codigo.....')
print('Fim.')