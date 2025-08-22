'''
3. Crie um programa que leia o nome de uma 
cidade e diga se ela começa ou não com o nome
'SANTO'.



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





'''
cores = {'limpa':'\033[m',
         'white-yellow':'\033[1;97;43m'}
nome_cidade = input('Digite uma cidade: ').upper().strip()
print(f'Essa cidade possui SANTO no nome: {cores["white-yellow"]}{nome_cidade.startswith('SANTO')}{cores['limpa']}')