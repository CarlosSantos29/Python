'''6.Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10
primeiros termos dessa progressão.'''
'''
termo = int(input('O valor do termo: '))
razao = int(input('O valor da razao: '))
termo_atual = termo

for contador in range(10 + 1):
    print(f'{contador}: termo: {termo_atual}\n', end=' ')
    termo_atual += razao
'''
termo = int(input('O valor do termo: '))
razão = int(input('O valor da razão: '))
pa = termo + (10 - 1) * razão

for contador in range(termo, pa + razão, razão):
    print(f'{contador}', end=' -> ')
print('final do codigo..,')
