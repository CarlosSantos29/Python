#metedos da classe list

#1. append() adicionar

lista = []

lista.append(21)
lista.append('Carlos')
lista.append([29,9,3])

print(lista)

#2. clear() limpar

print(lista) # [21, 'Carlos', [29,9,3]]

lista.clear()
print(lista)# []

#3. copy() copiar

lista = [1, 'Python', [40,30,20]]
lista.copy()
print(lista)

lista2 = lista.copy()
print(lista2)

print(id(lista2), id(lista))
lista[0] = 2

print(lista2)
print(lista)

#4. count() contar determinador valor existente na lista

cores = ['Vermelho', 'Azul', 'Verde', 'amarelo']

print(cores.count('Vermelho'))
print(cores.count('Azul'))
print(cores.count('Verde'))
print(cores.count('amarelo'))
print(cores.count('Amarelo'))

#5. extend() juntar listas

linguagens = ['python', 'node.js', 'C']
print(linguagens)
lista_2 = ['SQL','C#']
linguagens.extend(lista_2)
#linguagens.extend(['SQL','C#'])
print(linguagens)

#6. index() identificar a primeira aparição do valor na lista

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
linguagens.index('C#')#4
linguagens.index('python')#0

#7. pop() conceito de pilha, removendo os ultimos valores da lista ex: 01234 .pop()  = 0123

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']

print(linguagens.pop())# c#
print(linguagens.pop(-4))# python
print(linguagens.pop())# SQL
print(linguagens.pop(1))
print(linguagens.pop())

#8. remove() remove o valor solictado e existente na lista criada.

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
print(linguagens)
linguagens.remove('node.js')
print(linguagens)

#9. reverse() espelhar a lista

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
print(linguagens)
linguagens.reverse()
print(linguagens)

#10. sort ordenar os valores da lista
linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
print(linguagens)

linguagens.sort()
print(linguagens)

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
linguagens.sort(reverse=True)
print(linguagens)

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

#11. len() ler o tamanho da string ou valores de uma string

linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
print(len(linguagens))#5

#12. sorted
linguagens =  ['python', 'node.js', 'C', 'SQL','C#']
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
