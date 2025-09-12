def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')
#criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='Fiat', motor='1.0',combustivel='Gasolina')


def criar_carro2(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2('Palio',1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')
#criar_carro2(modelo='Palio', ano=1999, placa='ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

def somar_numero(a,b):
    return a + b

def multiplicar_numero(a,b):
    return a * b

def teste(a, b):
    return a * 2 + b * 2

def exibir_resultado(a, b, função):
    resultado = função(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')
    print(f'O resultado da operação {a} x {b} = {resultado}')

exibir_resultado(10, 10, somar_numero)
exibir_resultado(10, 10, multiplicar_numero)
exibir_resultado(3, 5, teste)

operação = somar_numero
print(operação(1,23))

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus # salario = salario + bonus
    return salario
#print(salario_bonus(500))
salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)


def salario_bonus2(bonus, lista):
    global salario
    #lista.append(2)
    lista_auxiliar = lista.copy()
    lista_auxiliar.append(2)
    print(f'lista auxiliar = {lista_auxiliar}')
    salario += bonus
    return salario

lista = [1]
salario_com_bonus2 = salario_bonus2(500, lista)
print(salario_com_bonus2)
print(lista)