# cores no terminal

print('\033[31mOlá mundo!')

print('\033[31;43mOlá mundo!')

print('\033[1;31;43mOlá mundo!')

print('\033[1;31;43mOlá mundo!\033[m')

print('\033[4;30;45mOlá mundo!\033[m')

print('\033[37mOlá mundo!\033[m')

print('\033[7;30mOlá mundo!\033[m')

print('\033[0;33;44mOlá mundo!\033[m')

print('\033[7;33;44mOlá mundo!\033[m')

a = 3
b = 5
print(f'Os valores são \033[33m{a} e \033[31m{b}')
print(f'Os valores são \033[33;42m{a}\033[m e \033[31;42m{b}\033[m')

nome = 'Carlos'
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m', 
         'azul-claro':'\033[93m',
         'verde-claro':'\033[92m',
         'inverte-cor':'\033[;7m'}

print(f'Bem-vindo!! {'\033[4;43m'}{nome}{'\033[m'}')


print(f'Bem-vindo!! {cores['verde-claro']}{nome}{cores['limpa']}')

print(f'Bem-vindo!! {cores['inverte-cor']}{nome}{cores['limpa']}')

#print corrigido - print(f"Bem-vindo!! {cores['amarelo_fundo']}{cores['vermelho']} {nome} {cores['limpa']}")
