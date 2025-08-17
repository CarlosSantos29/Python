#9. Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario_atual = float(input('Digite o salario atual do funcionario R$ '))
aumento_salario = salario_atual + (salario_atual * 15/100)
print(f'O salario do funcionario R$, com 15% de aumento ele comecará a receber R$ {aumento_salario:.2f}')