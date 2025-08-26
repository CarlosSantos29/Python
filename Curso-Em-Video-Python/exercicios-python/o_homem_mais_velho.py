'''soma = 0
media = 0
maiorIdadeHomem = 0
totalMulher = 0
nomeVelho = ''
for contador in range(1,5):
    print(f'----{contador}---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F)?')).strip()
    
    soma += idade
    
    if contador == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade > 20:
        totalMulher += 1
            
media = soma / 4
print(f'A media do grupo é de {media} anos')
print(f'O homem mais velhor tem {idade} anos e se chama {nome}')
print(f'Ao todo são {totalMulher} com menos de 20 anos.')'''

#irei corrigir

soma = 0
maior_idade_homem = 0
total_mulher = 0
nome_velho = ''

for contador in range(1,5):
    print('-'*5+f' {contador} '+'-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Qual seu genero? (M/F): '))
    soma += idade
  
    if sexo in 'Mm':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome
            
    
    if sexo in 'Ff' and idade < 20:
      total_mulher += 1
      
media_geral = soma / 4
print(f'A media geral de idade do grupo é igual a {media_geral} anos.')
print(f'Ao todo são {total_mulher} com menos de 20 anos.')

if maior_idade_homem > 0:
    print(f'A idade mais velha na média em geral é {maior_idade_homem} e a pessoa se chama {nome_velho}')
else:
    print(f'Não obteve homem(ns) no grupo.')