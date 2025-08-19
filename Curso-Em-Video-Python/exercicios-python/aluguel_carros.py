#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R0.15 por km rodado.

quantidade_km = float(input('Quantos Km foram percorridos? '))
quantidade_dias = int(input('Quantos dias o carro foi alugado? '))

preço_total = (quantidade_dias * 60) + (quantidade_km * 0.15)

print(f'De acordo com os dados solicitados, o valor total a pagar é de R${preço_total}')
