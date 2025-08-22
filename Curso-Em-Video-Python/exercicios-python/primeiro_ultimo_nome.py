
# parte ira quebra os espaços tranformando em lista.
nome_usuario = input('Digite o nome do usuario que está executando isso: ').strip().split()
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m', 
         'azul-claro':'\033[93m',
         'verde-claro':'\033[92m',
         'inverte-cor':'\033[;7m',
         'black-red':'\033[7;30;41m',
         'cyan-green':'\033[4;36;42m',
         'red-white':'\033[1;31;107m'}
print(f'O primeiro nome: {cores['red-white']}{nome_usuario[0]}{cores['limpa']}')  # primeiro nome.
# ultimo nome, notasse que está -1, porque como não tem noção do tamanho de espaço, o ultimo nome não aparece na lista.
print(f'O ultimo nome: {cores['azul-claro']}{nome_usuario[-1]}{cores['limpa']}')

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
