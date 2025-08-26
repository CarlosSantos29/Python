''''
esse codigo abaixo é generico, não possui linguagem em si, foi utizado como auxilio para a execução em python.
se n <= 1 então
    não é primo
senão
    para i de 2 até √n faça
        se n % i == 0 então
            não é primo
    fim-para
    é primo
fim-se
7. Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

from math import sqrt
numero = int(input('Digite um numero inteiro: '))
if numero <= 1:
    print(f'Esse {numero} não é primo.')
else:
    numero_primo = True
    
    for contador in range(2, int(sqrt(numero)) + 1):
        if numero % contador == 0 :
            numero_primo = False
            break
                   
    if numero_primo:  
        print(f'Esse {numero} é primo.')
    else:
        print(f'Esse {numero} não é primo.')'''

total_vezes = 0
numero = int(input('Digite um numero: '))
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[33m',end=' ')
        total_vezes += 1
    else:
        print('\033[31m', end=' ')
    print(f'{contador}',end=' ')
print(f'\n\033[mO numero {numero} foi divisivel {total_vezes} vezes.')

if total_vezes == 2:
    print('e concluindo, ele é primo. ')
else:
    print('e concluindo ele não é primo.')