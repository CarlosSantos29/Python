print('-x-'*5+' Gerador PA ' + '-x-'*5)
termo = int(input('Digite o valor do termo: '))
razao = int(input('Digite o valor da razão: '))
contador = 1
termoPA = termo
total_qntd = 0
mais_PA = 10
while mais_PA != 0:
    total_qntd += mais_PA
    while contador <= total_qntd:
        print(f'{termoPA} ->', end=' ')
        termoPA += razao
        contador += 1
    print('Pausa....')
    mais_PA = int(input('Deseja gerar mais alguns numeros PA? Quantos seriam? '))
print(f'fim do codigo...Progressão finalizada com {total_qntd} mostrados...')
