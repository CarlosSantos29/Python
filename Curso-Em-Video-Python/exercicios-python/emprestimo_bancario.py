'''
 Escreva um programa para aprovar o emprestimo bancario para a comprar de uma casa.
 O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos
 ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode
 exceder 30% do salario ou entao emprestimo será negado.
'''

valor_casa = float(input('Qual o valor do imovel? R$'))
salario_usuario = float(input('Seu salario atual? R$'))
anos_pagos = float(input('Em quantos anos deseja pagar? '))

numeros_parcelas = anos_pagos * 12
valor_prestacao_mensal = valor_casa / numeros_parcelas
limite_prestação = salario_usuario * 0.3

print(f'O valor total da prestação mensal R${valor_prestacao_mensal:.2f}')
print(f'Limite de pagamento com 30% do salario: R${limite_prestação:.2f}')



if valor_prestacao_mensal <= limite_prestação:
    print(f'Emprestimo aprovado!!')
else:
    print(f'Emprestimo Negado!!')