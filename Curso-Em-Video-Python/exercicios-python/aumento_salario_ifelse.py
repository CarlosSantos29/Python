'''
7.Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
para salarios superiores a R$ 1.250 calcule um aumento de 10%, para os inferiores e iguais
o aumento será de 15%.
'''
salario = float(input('Digite o salario atual do funcionario R$ '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'O novo salario do funcionario com 10% será R${aumento:.2f}')
else:
    aumento = salario + (salario * 15 / 100)
    print(f'O novo salario do funcionario com 15% de aumento será R${aumento:.2f}')
print('-'*5+'fim....')   