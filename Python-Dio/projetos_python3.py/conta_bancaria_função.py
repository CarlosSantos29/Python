'''
DESAFIO 

Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

OPERAÇÂO DEPOSITO

Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em 
identificar qual é o número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

OPERAÇÂO SAQUE

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que 
não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

OPERAÇÂO EXTRATO

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido
 o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

'''
from time import sleep
saldo = 0
valor = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def inicio_conta():
    while True:
        menu = int(input(f'''
    ============ BANCO GENERICO ==============
          [1]Depositar
          [2]Sacar
          [3]Extrato
          [4]Sair
    ==========================================
          --------> '''))
        if menu == 1:
            depositar()
        elif menu == 2:
            sacar()
        elif menu == 3:
            verificar_extrato()
        elif menu == 4:
            sair_menu()
            break
        else:
            print('Opção invalida.')

def depositar():
    global saldo, extrato
    valor = int(input('Diga o quanto deseja depositar R$ '))
    if valor > 0:
        saldo += valor
        extrato += f'O deposito realizado R$ {valor:.2f}\n'
        print('Saldo depositado com sucesso!')

def sacar():
    global saldo, numero_saques, extrato
    valor = int(input('Quanto deseja sacar? R$ '))
    if valor > saldo:
        print('Valor insuficiente.')
    elif valor > limite:
        print(f'Saque bloqueado, valor insuficiente, o limite disponivel é R$ {limite:.2f}')
    elif numero_saques >= LIMITE_SAQUES:
        print(f'Só está disponivel a realização de {LIMITE_SAQUES} saques.')
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque R$ {valor:.2f}\n'
        print('Saque realizado com sucesso.')
    else:
        print('Valor invalido para saque.')

def verificar_extrato():
    global extrato, saldo
    if not extrato:
        print('Não há nenhuma movimentaão inserida pelo usuario.')
    else:
        print(f'''
    ====INFORMAÇÕES GERAIS DO EXTRATO ====
        EXTRATO {extrato}
        SALDO ATUAL R$ {saldo:.2f}

    =====================================''')

def sair_menu():
    print('Saindo')
    sleep(2)
    print('.')
    sleep(2)
    print('.')
    sleep(2)
    print('.')
inicio_conta()
print('Fim da execução...')