'''
8. Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
(peso ÷ altura²).
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)

print(f'Você está pesando {peso:.1f}kg com altura de {altura:.1f}m')
print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Classificação: Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Classificação: Peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Classificação: Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Classificação: Obesidade.')
else:
    print('Classificação: Obesidade Mórbida.')