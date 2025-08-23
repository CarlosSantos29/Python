'''
5. Crie um programa que leia duas notas de um alunoo e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: Reprovado
- média entre 5.0 e 6.9: Recuperação
- media 7.0 ou superior: Aprovado
'''

nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))

media = (nota_1 + nota_2)/2
print(f'Media final: {media}')

if media < 5.0:
    print('REPROVADO!!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!!')