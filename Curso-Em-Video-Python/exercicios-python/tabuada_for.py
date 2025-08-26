'''4.Refaça o desafio 9, mostrando a tabuada de um numero que o usuario escolher, só que agora 
utilizando um laço for.'''
from time import sleep

print('='*5+' TABUADA '+'='*5)
numero = int(input('Digite um numero, veja sua Tabuada: '))

print('Carregando...')
sleep(2)
print('-#-'*4)
for contador in range(1, 11):
    print(f'{numero} x {contador:2} = {numero * contador}')
    
print('-#-'*4)