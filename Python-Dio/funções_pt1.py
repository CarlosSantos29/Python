#Função 1 que apenas exibe uma mensagem,
def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Seja Bem-Vindo {nome}')

def exibir_mensagem_3(nome='Default'):
    print(f'Seja Bem-Vindo {nome}')




exibir_mensagem()
#exibir_mensagem_2('Carlos')
exibir_mensagem_2(nome = 'Carlos')
exibir_mensagem_3('Eduardo')

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor
def function_3():
    print('Olá mundo! ')

print(calcular_total([10,10]))
print(retornar_antecessor_e_sucessor(5))
print(function_3())#Retorna um valor vazio

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro cadastrado com sucesso! {marca}/{modelo}/{ano}/{placa}')

#salvar_carro('Fiat','Palio','1999','ABC-1234')
#salvar_carro(marca='Fiat', modelo='Palio',ano='1999',placa='ABC-1234')
salvar_carro(**{'marca':'Fiat','modelo':'Palio','ano':'1999','placa':'ABC-1234'})#diionario

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('Sexta-feira, 26 de Agosto de 2022','Zen of Python', 'Beautigil is better than ugly.', autor='Tim Peters', ano=1999)