# if elif else

nome = str(input('Digite seu nome: ')).title()
if nome == 'Carlos':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal!')
print(f'Muito prazer em te conhecer, {nome}!!')

'''
exercicios ifelif else - python

1.
 Escreva um programa para aprovar o emprestimo bancario para a comprar de uma casa.
 O programa vai perguntar o valor da casa, o alario do comprador e em quantos anos
 ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode
 exceder 30% do salario ou entao emprestimo será negado. x
 
  
 2.
 Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher
 qual será a base da conversão:
 - 1 para binario bin()
 - 2 para octal oct()
 - 3 para hexadecimal. hex()      x
 
 3. 
Escreva um programa que leia dois numeros inteiros e compare os, mostrando na tela
uma mensagem: O primeiro valor é maior, o segundo é maior, não existe valor maior,
os dois são iguais.     x

4.
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade:
- se ele ainda vai se alistar ao serviço.
- se é a hora de se alistar.
- se ja passou do tempo do alistamento.     x

seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

5. Crie um programa que leia duas notas de um alunoo e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: Reprovado
- média entre 5.0 e 6.9: Recuperação
- media 7.0 ou superior: Aprovado     x

6. A confederação Nacional de Natação precisa de um prorgrama que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infatil
- Até 19 anos: Junior
- Até 20 anos: Senior
- Acima: Master         x

7. Refaça o desafio 35(Triangulos), acresentando o recurso de mostrar que tipo
de triangulo será formado:
-Equilatero Todos os lados iguais.
-Isoceles dois lados iguais.
-Escaleno: Todos os lados diferentes.  x

8. Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida     x

9. Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condiçãode pagamento:

- Á vista dinheiro/cheque: 10% de desconto.
- A vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros. x

10. Crie um programa que faça o computador jogar Jokenpo com você.
Tesoura corta Papel
Papel cobre Pedra
Pedra esmaga Lagarto
Lagarto envenena Spock
Spock esmaga (ou derrete) Tesoura
Tesoura decapita Lagarto
Lagarto come Papel
Papel refuta (ou refuta) Spock
Spock vaporiza Pedra
Pedra quebra (ou amassa) Tesoura 


'''
