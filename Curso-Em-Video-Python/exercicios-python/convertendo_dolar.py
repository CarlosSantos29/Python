#6. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere o valor atual.

dinheiro_disponivel = float(input('Quanto de dinheiro você tem disponivel? R$ '))
dolar = dinheiro_disponivel/5.25 #Valor atual no brasil.
print(f'O valor disponivel é R${dinheiro_disponivel} e você pode comprar ${dolar:.2f} em dolar.')

