'''
5. Faça um programa que leia uma frase pelo teclado
e mostre:
    - Quantas letras aparece a letra 'A'
    - Em que posição aparece a primeira vez.
    - Em que posição aparece pela ultima vez.
    
'''
nome_usuario = input('Digite o seu nome: ').upper().strip().replace(' ', '')
quantidade_a = nome_usuario.count('A')#essa variavel recebe a quantidade de letras A
primeira_posição = nome_usuario.find('A')#essa variavel recebe a posição da primeira letra A
ultima_posição = nome_usuario.rfind('A')#essa variavel recebe a ultima posição da letra A.

print(f'Seu nome: {nome_usuario}')
print(f'Total de A no nome solicitado: {quantidade_a}')
print(f'Primeira posição que aparece a letra A: {primeira_posição}')
print(f'Ultima posição que aparece a lletra A: {ultima_posição}')