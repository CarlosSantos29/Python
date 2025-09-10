nome = 'CarLOs'

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = '   ola mundo      '

print(texto + 'x')
print(texto.strip() + 'x')
print(texto.lstrip() + 'x')
print(texto.rstrip() + 'x')

menu = 'Python'
print('xxxx'+ menu + 'xxxx')
print(menu.center(14))
print(menu.center(14,'x'))
print('P-y-t-h-o-n')

for letra in menu:
    print(letra, end='-')
print()

print('-'.join(menu))