print('Olá, Mundo!')

print(7 + 4)

print('7'+'4')

print('Olá', 10)#Certo

#print('Olá'+10) - errado

nome = 'Carlos'
idade = 21
peso = 74

print(f'Olá {nome} você tem {idade} anos, e seu peso é {peso}kg, correto? ')#Atual formatação em python.
#print(nome, idade, peso) forma certa de formatar numeros.
#print(nome + idade + peso) Forma errada de formatar numeros.

nome_2 = input('Qual seu nome? ')
idade_2 = input('Atualmente qual a sua idade? ')
peso_2 = input('Você pesa quanto atualmente? ')

print('Olá {} você tem {} anos e atualmente pesa {}kg'.format(nome_2, idade_2, peso_2))#Antiga formatação de variaveis em python.