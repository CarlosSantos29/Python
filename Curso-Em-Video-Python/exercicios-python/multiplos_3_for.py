'''3.Faça um programa que calcule a soma entre os numeros impares que sao multiplos de três e que
se encontram no intervalo de 1 até 500.'''

#varivel soma de inicio começa no 0, facilitando o processo no for
soma = 0
cont = 0
#configuração para contar de 1 até 500, incluindo o 500
for contador in range(1, 501, 2):
    #Calculando e pedindo para o contador exibir o a somatoria se caso for multiplo de 3 e que não fosse divisivl por 2 == 0
    if contador % 3 == 0: #and contador % 2 != 0:
        soma += contador # soma = soma + contador
        cont += 1
        print(f'Soma = {soma} + {contador}')
#Total da soma de numeros impares, multiplos de 3
#print(f'A soma total dos impares multiplos de 3 é igual a: {soma}')
print(f'A soma de todos os {cont} valores solicitados é {soma}.')