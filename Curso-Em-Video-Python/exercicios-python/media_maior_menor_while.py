'''9. Crie um programa que leia varios numeros inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual foi o
maior e o menor valores lidos. O programa deve perguntar ao usuario
se ele quer ou não continuar a digitar valores.
'''

soma = 0
quantidade = 0
maior = None
menor = None


while True:
    resposta = str(input('Deseja adicionar um valor? (Sim/não): ')).upper()
    if resposta == 'N':
        print('Saindo do codigo...')
    elif resposta == 'S':
        numero = int(input('Digite um valor: '))
        soma += numero
        quantidade += 1
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero
    else:
        print('Opção invalida...')


print(f'O maior numero: {maior} e o Menor numero: {menor}')