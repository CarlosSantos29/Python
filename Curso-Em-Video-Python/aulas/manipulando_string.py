'''
#fatiamento
variavel[0] - letra
variavel[0:0] - inicio e o fim do fatiamento
variavel[0:0:0] - inicio, fim, pulando 
variavel[:0] - do inicio até o valor solicitado.
variavel[0:] - inicio até o fim
variavel[0::0] - do inicio ate o fim pulando.

#analise
len(variavel) - comprimento da variavel/string.

variavel.count('') - contar quantas vezes aparece
o caracter solicitado.

variavel.count('',0,0) - contagem com fatiamento, do
inicio até o valor solicitado, verificando quantos 
caracteres solicitado na virgula existe.

varivael.find('') - encontrar onde o caracter solicitado começa.

variavel.find('inexistente') - retorna -1/não encontrado.

'String' in variavel - se a string em aspas existe 
na variavel criada, retornando um valor booleano.

#transformação
variavel.replace('','') - Alterar um texto existente
por outro., de forma secundaria.

variavel.upper() - maiusculo

frase.lower() - minusculo

variavel.capitalize() - primeira letra do 
primeiro caracter em maiusculo.

variavel.title() - primeira letra de cada palavra 
no texto/string em maisuculo.

variavel.strip() - remove espaços do inicio e o fim.

variavel.rstrip() - remove os ultimos espaços do
texto/string.

varivael.lstrip() - remove espaços do inicio.

#divisão
variavel.split() - verifica se existem espaços,
quebra e divide as palavras, criando uma lista
para cada um.

#junção
''.join(variavel) - juntar os elementos divididos
ou não, adicionando o caracter solicitado por
aspas simples/duplas.
'''

frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('Oi')

print('''Welcome! Are you completely new to programming?
about why and now to get started with Python. Fortunately
an experienced programmer in any programmin language
(whatever it may be) can pick up Python very quickly.
Its also esay for beginners to use and learn, so
jump!''')  # forma facil de printar um texto completo.

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper())
print(frase.upper().count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase.replace('Python', 'Ubuntu'))
# frase = print(frase.replace('Python','Ubuntu'))
print('Curso' in frase)
print(frase.find('curso'))
print(frase.find('Curso'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

'''
exercicios

1. Crie um programa que leia o nome completo
da pessoa e mostre:
    - O nome com todas as letras maisculas.
    - O nome com todas minusculas.
    - Quantaaas letras ao todo(sem considerar
    espaços.)
    - quantas letras tem o primero nome.
    
2. Faça um programa que leia 
um numero de 0 a 9999 e mostre
na tela cada um dos digitos separados.
ex: Digite um numero: 1834.

unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

3. Crie um programa que leia o nome de uma 
cidade e diga se ela começa ou não com o nome
'SANTO'.

4.Crie um programa que leia o nome de uma pessoa
e diga se ela tem 'SILVA' no nome.

5. Faça um programa que leia uma frase pelo teclado
e mostre:
    - Quantas letras aparece a letra 'A'
    - Em que posição aparece a primeira vez.
    - Em que posição aparece pela ultima vez.
    
6. Faça um programa que leia o nome completo    
de uma pessoa, mostrando em seguida o primeiro e
o ultimo nome separadamente.

ex: Ana Maria de Souza
Primeiro: Ana   Ultimo: Souza    
    
'''
