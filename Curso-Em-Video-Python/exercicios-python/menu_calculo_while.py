'''3.Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa

seu programadeverá realizar a operação solicitada em cada caso.
'''
from time import sleep
print('-'*5+' Escolha os dois numeros '+'-'*5)
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
opção = 0
print('-'*5+' Menu Matematico '+'-'*5)
while opção != 5:
    
    opção = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n\nEscolha aqui: '))
    sleep(2)
    if opção == 1:
        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif opção == 2:
        print(f'{numero_1} x {numero_2} = {numero_1 * numero_2}')
    elif opção == 3:
        if numero_1 == numero_2:
            print('Ambos os numeros são iguais.')
        elif numero_1 > numero_2:
            print(f'O maior numero é o {numero_1}')
        else:
            print(f'O maior numero é o {numero_2}')
    elif opção == 4:
        numero_1 = int(input('Digite um primeiro novo valor: '))
        numero_2 = int(input('Digite um segundo novo valor: '))
    elif opção == 5:
        print('Saindo do menu....')
        sleep(2)
    else:
        print('Opção invalida..')
print('Fim do codigo...')
