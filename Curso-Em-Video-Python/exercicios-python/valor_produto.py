'''
9. Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condiçãode pagamento:

- Á vista dinheiro/cheque: 10% de desconto.
- A vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''
valor_produto = float(input('Digite o valor do produto? R$ '))
escolha_pagamento = int(input('1- A vista dinheiro/cheque.\n2- A vista no cartão.\n3x ou mais no cartão.\nAguardando sua resposta: '))

if escolha_pagamento == 1:
    desconto = valor_produto * 0.9
    print(f'O valor a ser pago com 10% de desconto a vista no dinheiro ou cheque será R${desconto:.2f}')
elif escolha_pagamento == 2:
    desconto = valor_produto * 0.95
    print(f'O valor a ser pago com 5% de desconto a vista no cartão será R$ {desconto:.2f}')
elif escolha_pagamento == 3:
    parcelas = int(input('Informe o numero de parcelas: '))
    if parcelas >= 3:
        valor_final = valor_produto * 1.2
        valor_parcela = valor_final / parcelas
        print(f'O valor do juros de 20% R${valor_final:.2f}')
        print(f'Parcelado em {parcelas}x de R$ {valor_parcela:.2f}')
    elif parcelas == 2:
        valor_final = valor_produto
        valor_parcela = valor_final
        print(f'Parcelado em 2x de R$ {valor_parcela:.2f}')
    else:
        print('Numero de parcelas invalido.')
else:
    print('Opção invalida.')