'''
7. Refaça o desafio 35(Triangulos), acresentando o recurso de mostrar que tipo
de triangulo será formado:
-Equilatero Todos os lados iguais.
-Isoceles dois lados iguais.
-Escaleno: Todos os lados diferentes.
'''

lado_1 = float(input('Digite o L1: '))
lado_2 = float(input('Digite o L2: '))
lado_3 = float(input('Digite o L3: '))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    triangulo = True
else:
    triangulo = False
    
print(f'L1: {lado_1}\nL2: {lado_2}\nL3: {lado_3}')
print(f'Pode formar triangulo? {triangulo}')

if lado_1 == lado_2 == lado_3:
    print('e esse triangulo pode ser equilatero.')
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('e esse triangulo pode ser isoceles.')
elif lado_1 != lado_2 != lado_3:
    print('e essetriangulo pode ser escaleno.')
else:
    print('Não é possivel formar triangulo>')