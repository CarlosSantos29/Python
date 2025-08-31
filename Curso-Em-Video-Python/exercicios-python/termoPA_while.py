print('-x-'*5+' Gerador PA ' + '-x-'*5)
termo = int(input('Digite o valor do termo: '))
razao = int(input('Digite o valor da razão: '))
contador = 1
termoPA = termo

while contador <= 10:
    print(f'{termoPA} ->', end=' ')
    termoPA += razao
    contador += 1
print('Fim do codigo....')