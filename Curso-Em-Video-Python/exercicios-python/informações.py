'''1. Crie um programa que leia o nome completo
da pessoa e mostre:
    - O nome com todas as letras maisculas.
    - O nome com todas minusculas.
    - Quantaaas letras ao todo(sem considerar
    espaços.)
    - quantas letras tem o primero nome.'''

nome_usuario = str(input('Digite seu nome completo: '))
print(f'Nome como todas as letras em maiuscula: {nome_usuario.upper()}')
print(f'Nome com todas as letras em minusculas: {nome_usuario.lower()}')
print(f'Quantidade de letras ao todo (sem considerar espaços): {len(nome_usuario.replace(" ", ""))}')
modificação = nome_usuario.split()
print(f'O numero total do primeiro nome: {len(modificação[0])}')
