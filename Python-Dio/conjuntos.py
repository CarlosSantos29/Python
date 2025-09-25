#1 set() elimina valores duplicados em uma lista.

print(set([1, 2, 3, 1, 3, 4]))
print(set('abacaxi'))
print(set(('palio','gol','celta','palio',)))

linguagens = {'python', 'java', 'python'}
print(linguagens)

numeros = {1,2,3,4}
numeros = list(numeros)
print(numeros[-4])

carros = {'palio','gol','celta'}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')

#2,union() | Junção de conjuntos

conjunto_a = {1,2}
conjunto_b = {3,4}
print(conjunto_a.union(conjunto_b))# 1,2,3,4

#3. intesection() & valores que existem em ambos os conjuntos

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.intersection(conjunto_b))#2,3

#4. difference() - valores que existem no conjunto A mas não no B

conjunto = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))#1
print(conjunto_b.difference(conjunto_a))#4

#5. symmetric_difference() ^ valores que não se repetem em ambos os conjuntos

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.symmetric_difference(conjunto_b))# 1,4

#6 issubset() <= verificar se um conjunto é subconjunto de outro

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b))#True
print(conjunto_b.issubset(conjunto_a))#False

#7. issuperset() >= verificar se um conjunto é superconjunto de outro

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issuperset(conjunto_b))#False
print(conjunto_b.issuperset(conjunto_a))#True

#8 isdisjoint'() verificar se não há valores iguais entre os conjuntos

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}
print(conjunto_a.isdisjoint(conjunto_b))#True
print(conjunto_a.isdisjoint(conjunto_c))#False

#9 add() adicionar valores ao conjunto

sorteio = {1,23}
sorteio.add(25)# 1,23,25
sorteio.add(42)# 1,23,25,42
sorteio.add(25)#Não adiciona valores repetidos
print(sorteio)

#10. clear() limpar o conjunto

sorteio = {1,23}
sorteio.clear()#{}
print(sorteio)

#11. copy() copia o conjunto
sorteio = {1,23}
sorteio.copy()
print(sorteio)

#12. discard() remove o valor solicitado, sem gerar erro caso o valor não exista

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.discard(1)
numeros.discard(5)
numeros.discard(45)
print(numeros)

#13> pop() remove o valor em forma de pilha, ou seja, o ultimo valor adicionado

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.pop()
numeros.pop()

print(numeros)

#14. remove() remove o valor solicitado, gerando erro caso o valor não exista

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros.remove(5)
print(numeros)

#15. len() tamanho do conjunto

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
print(len(numeros))#10