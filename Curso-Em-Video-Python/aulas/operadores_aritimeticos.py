#ordem de precedencia
'''
1. ()
2. **
3. * / // %  (quem aparecer primeiro na linha de codigo será executado e calculado.)
4. + -

>>> 4**3
64
>>> pow(4,3)
64
>>> 81**(1/2)
9.0
>>> 25**(1/2)
5.0
>>> 127**(1/3)
5.026525695313479
>>> clear
>>> 'oi' + 'ola'
'oiola'
>>> 'oi'*5
'oioioioioi'
>>> '='*20
'===================='
>>> print('='*20)
====================

'''

nome = input('Qual é seu nome? ')
print(f'Prazer em te conher {nome:20}!')
print(f'Prazer em te conher {nome:>20}!')# alinhamento a direita
print(f'Prazer em te conher {nome:<20}!')# alinhamento a esquerda
print(f'Prazer em te conher {nome:^20}!')# alinhado no centro
print(f'Prazer em te conher {nome:=^20}!')# alinhado no centro adicionando o simbolo no espaço restante.


#operadores arimeticos
numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite o segundo numero: '))

soma = numero_1 + numero_2
subtracacao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
exponenciacao = numero_1 ** numero_2

print(f'A soma vale tanto: {soma}.', end = ' || ')
print(f'A subtração vale: {subtracacao}.', end = ' || ')
print(f'A multiplicação vale: {multiplicacao}.', end = ' || ')
print(f'A divisão vale: {divisao:.3f}.', end = ' || ')
print(f'A divisão por inteira vale: {divisao_inteira}.', end = ' || ')
print(f'A exponenciação do numero vale: {exponenciacao}.')

