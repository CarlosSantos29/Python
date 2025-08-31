numero = int(input('Digite o valor do termo: '))
termo_1 = 0
termo_2 = 1
contador = 3 # esse valor porque o termo 1 e o termo 2 ja foram somados, entao o contador apartir do proximo termo começa no 3.
print(f'{termo_1} -> {termo_2}', end=' -> ')
while contador <= numero:
    termo_3 = termo_1 + termo_2
    print(f'{termo_3} -> ', end =' -> ')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(' Fim do codigo....')