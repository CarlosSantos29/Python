# O uso do IF/ELSE
'''
nome_usuario = str(input('Qual seu nome: '))
if nome_usuario == 'Carlos':
    print('Que nome bonito!!')
else:
    print('Seu nome é tão normal. :( ')
print(f'Bom Dia senhor(a) {nome_usuario}!!')

'''
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_media = (nota_1 + nota_2) / 2

'''
# Com todo respeito, essa daqui é a melhor forma de usar estruturas condicionais.
if nota_media >= 6:
    print('Parabens, nota excelente, APROVADO!')
else:
    print('Nota pessima :( melhore mais, REPROVADO!')
'''
print('Analisando sua média final...')
print(f'{nota_1} + {nota_2} = {nota_media}')
print('Aprovado' if nota_media >= 6 else 'Reprovado!')
print('-'*5 + 'Fim do codigo...')

'''
EXERCICIOS IF/ELSE (SEM O USO DO ELIF)

1.escreva uma programa que faça o computador pensar em um numero inteiro
entre o 0 e 5, e peça para o usuario tentar descobrir qual foi o numero escolhido
pelo computador.
o programa deverá escrever na tela se o usuario venceu ou perdeu.

2.Escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7 por cada km acima do limite.
calculo para multa -- variavel_multa = (variavel_velocidade - 80) km x R$7

3. Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.
(variavel % 2 == 0)

4. Desenvolva um programa que pergunte a distancia de uma viagem em Km.
calcule o preço da passagem, cobrando 50 centavos por km para viagens de até 200km
e 45 centavos para viagens mais longas.
 - Se a distância for até 200 km, o preço será:
variavel_istância x R$0,50  
 - Se a distância for maior que 200 km, o preço será:
varivael_distância x R$0,45

5.Faça um programa que leia o ano qualquer e mostre se ele é bissexto.
variavel bissexto / 4 e / 400.

6.Faça um programa que leia 3 numeros, e mostre qual é o maior e qual é o menor.
calculo -> para descobrir o maior =  A > B e A > C, senão B > A e B > C (if if else)

7.Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
para salarios superiores a R$ 1.250 calcule um aumento de 10%, para os inferiores e iguais
o aumento será de 15%.

8. Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas
podem ou não formar um triangulo. A+B>C e A+C>B e B+C>A
'''