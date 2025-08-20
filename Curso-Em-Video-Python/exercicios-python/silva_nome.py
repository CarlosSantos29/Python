'''
4.Crie um programa que leia o nome de uma pessoa
e diga se ela tem 'SILVA' no nome.
'''
nome_usuario = input('Digite seu nome: ').upper()
verificar_nome = 'SILVA' in nome_usuario
print(f'O seu nome: {nome_usuario}\nPossui SILVA no nome? {verificar_nome}')