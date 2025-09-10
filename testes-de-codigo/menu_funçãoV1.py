'''nome do usuario
def 

'''
def exibir_menu():
    while True:
        try:
            opção = int(input(f'''
        ============== MENU MATEMATICO V1.0 ===============
        Olá, seja bem-vindo :) então, o que deseja realizar?     

        1 - Somar numero
        2 - Fatorial de um numero
        3 - Adivinhe um numero
        4 - impar e par
        5 - sair
    
    Digite aqui: '''))
            if opção == 1:
                somar_valores()
            elif opção == 2:
                fatorial_numero()
            elif opção == 3:
                adivinhe_numero()
            elif opção == 4:
                numeros_pares_impares()
            elif opção == 5:
                saindo_menu()
                break
            else:
                print('Opção invalida..')
        except ValueError:
                print('Digite um valor valido..')
    
        
def somar_valores():
    numero_1 = int(input('Digite o primeiro valor: '))
    numero_2 = int(input('Digite o segundo valor: '))
    return print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')

def fatorial_numero():
    from math import factorial
    numero_1 = int(input('Digite um valor e veja sua fatorial: '))
    contador = numero_1
    print(f'{numero_1}! = ',end=' ')
    while contador > 0:
        print(f'{contador} ',end='')
        print('x' if contador > 1 else '=', end=' ')
        contador -= 1
    print(f'{factorial(numero_1)}', end=' ')

def adivinhe_numero():
    from random import randint
    jogador = int(input('Tente adivinhar em um numero em que a maquina adivinhou.... Digite seu valor: '))
    maquina = randint(1,10)
    if jogador == maquina:
        print('Parabens!!! você adivinhou o numero que o computador pensou.')
    else:
        print('Não foi dessa vez..')
            
    print(f'escolha do jogador: {jogador}\nEscolha da maquina: {maquina}')

def numeros_pares_impares():
    numero_1 = int(input('Digite um valor e veja se ele é um valor par ou impar: '))
    if numero_1 % 2 == 0:
        print(f'O numero solicitado: {numero_1}, e ele é par.')
    else:
        print(f'O numero solicitado: {numero_1} e ele é impar.')

def saindo_menu():
    from time import sleep
    for contador in range(3, -1, -1):
        print(f'{contador}')
        sleep(2)
    print('Fim do codigo...')

exibir_menu()