#Conteúdo dedicado no aprendizado de tuplas em Python

frutas_1 = ('laranja', 'pera', 'uva',)
print(frutas_1)

letras = tuple('Python')
print(letras)

numeros = tuple([1, 2, 3, 4, 5])
print(numeros)

pais = ('Brasil',)
print(pais)

frutas_2 = ('maçã', 'laranja', 'uva', 'pera',)#0 1 2 3
print(frutas_2[0])#maçã
print(frutas_2[2])#uva
print(frutas_2[-1])#pera
print(frutas_2[-3])#laranja
print(frutas_2[-4])#maçã

               #0           #1         #2
matriz = ((1, 'a', 2), ('b',3 ,4), (6, 5, 'c'))#0 1 2
print(matriz[0])# 1 a 2
print(matriz[0][0])# 1
print(matriz[0][-1])# 2
print(matriz[-1][-1])# c

#tupla = ('python',)
tupla = tuple('python')

print(tupla[2:])#t h o n
print(tupla[:2])#p y
print(tupla[1:3])#y t
print(tupla[0:3:2])#p t
print(tupla[::])# p y t h o n
print(tupla[::-1])# n o h t y p

carros = ('gol', 'celta', 'palio',)

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')


cores = ('red', 'yellow', 'black', 'black',)
print(cores.count('red'))#1 vez
print(cores.count('yellow'))#1 vez
print(cores.count('black'))#2 vezes

linguagens = ('python', 'js', 'c', 'java', 'c#',)
#linguagens = tuple(['python', 'js', 'c', 'java', 'c#'])

print(linguagens.index('java'))#3
print(linguagens.index('python'))#0
print(linguagens.index('js'))#1

linguagens = ('python', 'js', 'c', 'java', 'c#',)
print(len(linguagens))#