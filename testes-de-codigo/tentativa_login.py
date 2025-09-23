from time import sleep
nome = ''
senha = 0

def novo_perfil():
    novo_usuario = 0
    while novo_usuario != 3:
        global nome, senha, confirmar_senha
        novo_usuario = int(input(f'''
    ==============================
     Acesso Usuario, Olá inicie sua sessão, 
    caso seja novo crie uma nova conta.
                [1 Login]
                [2 Cadastrar]
                

    ----> '''))
        if novo_usuario == 1:
            perfil()
        elif novo_usuario == 2:
            cadastar_login()
        elif novo_usuario == 3:
            sair()
            break
        else:
            print('Opção invalida..')

def perfil():
    global nome, senha, confirmar_senha, novo_usuario
    nome = input('Digite seu nome: ')
    senha = int(input('Digite sua senha: '))

def cadastar_login():
    global nome, senha, confirmar_senha
    nome = input('Digite um nome para o usuario: ')
    senha = int(input('Digite uma senha para o usuario: '))
    confirmar_senha = int(input('Digite novamente a senha: '))

    if senha == confirmar_senha:
        nome = nome
        senha = senha
        print(f'''
    =============================
        Informações Cdastradas
        
        nome usuario = {nome}
        senha criada = {senha}
''')
    else:
        print('Informações invalidades, confirme corretamente e tente novamente.')
    print('Voltando pro menu...')
    sleep(2)
def sair():
    print('Saindo...')
novo_perfil()