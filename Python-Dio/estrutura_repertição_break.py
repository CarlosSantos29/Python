escolha = -1

'''
while escolha != 0:
    escolha = int(input('Informe um numero\n'))
    if escolha % 2 == 0:
        print(escolha)
        escolha = int(input('Informe um numero\n'))
    else:
        break'''


while escolha != 0:
    escolha = int(input('Informe um numero\n'))
    
    if escolha == 10:
        break
    else:
        print(f'Numero: {escolha}')
print('fim do codigo....')