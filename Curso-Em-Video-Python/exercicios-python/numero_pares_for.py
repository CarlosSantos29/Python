#2.Faça um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.

#Usando o for e o if informei de 1 a 50 os numeros pares
'''
for contador in range(1, 50 + 1):
    if contador % 2 == 0:
        print(contador, end=' ')'''
        
for contador in range(2, 51, 2):
    print(contador, end=' ') 