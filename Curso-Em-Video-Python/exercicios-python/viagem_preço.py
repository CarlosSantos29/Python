'''
4. Desenvolva um programa que pergunte a distancia de uma viagem em Km.
calcule o preço da passagem, cobrando 50 centavos por km para viagens de até 200km
e 45 centavos para viagens mais longas.
 - Se a distância for até 200 km, o preço será:
variavel_istância x R$0,50  
 - Se a distância for maior que 200 km, o preço será:
varivael_distância x R$0,45
'''
distancia = float(input('Qual a distancia percorrida?  '))

print('Calculando....')
if distancia <= 200:
    calculo_distancia = distancia * 0.5
    print(f'Distancia percorrida: {distancia}km')
    print(f'O valor total da passagem: R${calculo_distancia:.2f}')
else:
    calculo_distancia = distancia * 0.45
    print(f'Distancia percorrida: {distancia}km')
    print(f'O valor total da passagem: R${calculo_distancia:.2f}')
print('-'*5+'Fim do código...')