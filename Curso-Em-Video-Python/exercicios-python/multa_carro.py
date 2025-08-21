'''
2.Escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7 por cada km acima do limite.
calculo para multa -- variavel_multa = (variavel_velocidade - 80) km x R$7
'''

velocidade = float(input('Quanto carro percorreu? '))

print('Calculando km percorridos...')
if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print(f'Km percorrido: {velocidade}km')
    print(f'Valor da multa R${valor_multa:.2f}')
    print('Você ultrapassou os 80km, será multado!')
else:
    print(f'Km percorrido: {velocidade}km, dirija com segurança.')
print('-'*5+' Fim...')
    