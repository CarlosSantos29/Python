'''
8. Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas
podem ou não formar um triangulo. A+B>C e A+C>B e B+C>A


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



'''

lado_1 = float(input('Digite o primeiro lado: '))
lado_2 = float(input('Digite o segundo lado: '))
lado_3 = float(input('Digite o terceiro lado: '))
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m', 
         'azul-claro':'\033[93m',
         'verde-claro':'\033[92m',
         'inverte-cor':'\033[;7m',
         'black-red':'\033[7;30;41m',
         'cyan-green':'\033[4;36;42m'}
print('Calculando...')
if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    triangulo = True
else:
    triangulo = False
print(f'{cores['black-red']}L1:{cores['limpa']} {lado_1}\n{cores['verde-claro']}L2:{cores['limpa']} {lado_2}\n{cores['cyan-green']}L3:{cores["limpa"]} {lado_3}')
print(f'De acordo com os dados obtidos, pode formar um triangulo? {triangulo}')
print('-'*5+' Fim do codigo....')