#Trabalhando com listas em Python pt1

frutas = ['Laranja', 'Maça', 'Uva']
print(frutas)

frutas =[]
print(frutas)

letras = list('Python')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]
print(carro)

#Buscando valor diretamente

frutas = ['Maça', 'Laranja', 'Uva', 'Pera'] # 0 1 2 3
print(frutas[3])#Pera
print(frutas[0])#Maça

#Indices negativos (de trás para frente)

frutas = ['Maça', 'Laranja', 'Uva', 'Pera']# -1 -2 -3 -4
print(frutas[-4])#Maça
print(frutas[-2])#Uva

#Listas aninhadas

matriz = [[5, 'b', 3],['d','4',9],[6,3,8]]#linhas 0 1 2, colunas 0 1 2, puxando ultimos valores(linhas e colunas) -1 -2 -3

print(matriz[2])#[6,3,8]
print(matriz[1][2])#9
print(matriz[1][-3])#'d'
print(matriz[-1][-1])#8

#Fatiamento

lista = list('Python')# 0 1 2 3 4 5
print(lista[2:])# t h o n
print(lista[:2])# P y
print(lista[1:3])# y t
print(lista[0:3:2])# p t
print(lista[::])# p y t h o n
print(lista[::-1])# n o h t y p (de trás para frente)

#interar listas

carros = ['Ferrari', 'Jeep', 'Gol']

for carro in carros:
    print(f'- {carro}')

#Função enumerate 0 1 2... com a função for

carros = ['Ferrari', 'Jeep', 'Gol']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

# Compreensão de listas

numeros = [0, 30, 21, 2, 9, 65 , 34]
pares = []# 0 2 21...

#versão 1
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)
        print(pares)

#versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Modificando valores

#versão 1

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

#versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

