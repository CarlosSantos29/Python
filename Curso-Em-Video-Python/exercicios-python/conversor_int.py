''' Escreva um programa que leia um 
numero inteiro qualquer e peça para o 
usuario escolher qual será a base da conversão:
 - 1 para binario bin()
 - 2 para octal oct()
 - 3 para hexadecimal. hex()
 

text                    background
 
30      black       preto          40
31      red           vermelho   41
32      green       verde         42
33      yellow      amarelo    43
34      blue          azul           44
35      Magenta  Magenta  45
36      cyan         ciano         46
37      grey          cinza         47
97      white        branco     107


style = 0(default) 1(negrito) 4(sublinhado) 7(inverte a cor)


cores = {'limpa':'\033[m',
         'vermelho':'\033[31m', 
         'azul-claro':'\033[93m',
         'verde-claro':'\033[92m',
         'inverte-cor':'\033[;7m',
         'black-red':'\033[7;30;41m',
         'cyan-green':'\033[4;36;42m'
         }

'''
from time import sleep
numero = int(input('Digite um valor: '))
escolha = int(input(
    'escolha qual base numerica deseja converter:\n1- Binario\n2- Octal\n3- Hexadecimal\nAguardando sua resposta:'))

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'azul-claro': '\033[93m',
         'verde-claro': '\033[92m',
         'inverte-cor': '\033[;7m',
         'black-red': '\033[7;30;41m',
         'cyan-green': '\033[4;36;42m'
         }


print(f'{cores['azul-claro']}Calculando...{cores['limpa']}')
sleep(2)

if escolha == 1:
    print(f'O numero solicitado pelo usuario: {numero}')
    print(f'Convertido em binario: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O numero solicitado pelo usuario: {numero}')
    print(f'Convertido em octal: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O numero solicitado pelo usuario: {numero}')
    print(f'Convertido em hexadecimal: {hex(numero)[2:]}')
else:
    print('Opção inválida.')
print('-'*5+'Fim....')
