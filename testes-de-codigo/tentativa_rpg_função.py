from time import sleep

exp = 0  # variável global para XP


def iniciar():
    opção = int(input(f'''
    ============= Adventure RPG Demo =====================
    
                        [1] Novo Jogo
                        [2] Instruções

----> '''))
    if opção == 1:
        criar_personagem()


def criar_personagem():
    entrada = input(f'''
    Escreva o seguinte formulário (nome, classificação herói, idade)
----> ''')
    
    nome, classificacao, idade = entrada.split(',')

    confirmar = input(f'''
        =========== Confirma as informações? ===================
            Nome: {nome.strip()}
            Classificação: {classificacao.strip()}
            Idade: {idade.strip()}

Se os dados estão corretos, deseja começar o modo história? (Sim/Não)
----> ''').upper()

    if confirmar == 'S' or confirmar == 'SIM':
        modo_historia()


def modo_historia():
    input(f'''
O ano era 1990, em Milano, Itália...
(... história ...)
O que deseja fazer, nobre guerreiro? 
    [1] Explorar
    [2] Ver os itens

----> ''')
    explorar()  # Agora a função será chamada


def explorar():
    escolha = int(input(f'''
    ========= Floresta Dark ============
    Você entra em uma floresta destruída...
    Você encontra o primeiro inimigo.
    O que deseja fazer?

        [1] Atacar
        [2] Fugir

----> '''))
    if escolha == 1:
        atacar()
    else:
        print("Você fugiu! Fim da aventura.")


def atacar():
    global exp
    exp += 5
    confirmar_2 = input(f'''
Você atacou o inimigo e ganhou 5 XP!
Total de XP: {exp}
================================================
Deseja continuar explorando? (Sim/Não)
----> ''').upper()

    if confirmar_2 == 'SIM' or confirmar_2 == 'S':
        input(f'''
Você matou o inimigo e encontrou rastros.
Eles levam até uma ponte que cruza para uma vila misteriosa...
Enquanto explora a vila...

Continua......
            ==== Obrigado por jogar a Demo =====''')    
        '''
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)'''
        #explorar()  # Continua a jornada
        
    else:
        print("Aventura encerrada. Obrigado por jogar!")


iniciar()
