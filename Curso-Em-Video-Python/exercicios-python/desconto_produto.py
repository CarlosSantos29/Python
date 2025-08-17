#8.Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do produto R$ '))
desconto = produto - (produto * 5/100)
print(f'O valor do produto escolhido R$ {produto:.2f} aplicando 5% de desconto, fica R$ {desconto:.2f}')