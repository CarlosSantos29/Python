'''
Fluxo de um sistema de lista de afazeres em Python
Início do programa


Criar uma estrutura de dados vazia (ex.: uma lista chamada tarefas).


Entrar em loop (while)


Enquanto o usuário não pedir para sair, o programa continua rodando.


Exibir menu de opções


Mostrar opções como:


1 → Adicionar tarefa


2 → Remover tarefa


3 → Listar tarefas


4 → Sair


Usuário escolhe uma opção


O programa lê a escolha e direciona para a ação correspondente.


Adicionar tarefa


Perguntar qual tarefa o usuário quer adicionar.


Usar a lista (ou dicionário) para armazenar essa nova entrada.


Remover tarefa


Perguntar qual tarefa remover.


Verificar se ela existe na lista/dicionário.


Se existir, remover. Se não, avisar que não foi encontrada.


Listar tarefas


Mostrar todas as tarefas atualmente salvas.


Se não houver nenhuma, avisar que a lista está vazia.


Sair


Encerrar o loop while e finalizar o programa.

'''
meus_dados = {}

def gerenciador_tarefas():
    while True:
        confirmar_escolha = int(input(f'''
        
        [Gerenciador de Tarefas]

        [1] Adicionar tarefa
        [2] Analisar tarefas existentes
        [3] Remover tarefa
        [4] Tarefas concluidas
        [5] Sair

Digite aqui a opção que deseja ---> '''))
        if confirmar_escolha == 1:
            adicionar_tarefas()
        elif confirmar_escolha == 2:
            analisar_tarefa()
        elif confirmar_escolha == 3:
            remover_tarefas()
        elif confirmar_escolha == 4:
        '''será adicionado ainda'''
        elif confirmar_escolha == 5:
                break            

def adicionar_tarefas():
    tarefa_chave = input('diga um titulo para sua tarefa --> ')
    tarefa_valor = input('Digite o que deseja adicionar uma nova tarefa --> ')
    meus_dados[tarefa_chave] = tarefa_valor 
    print(f'''[Gerenciador de Tarefas]
          
          - Tarefa adicionado com sucesso.
          - Tarefa adicionada --> {tarefa_valor}''')
    
def analisar_tarefa():
    print(f'''
        [Gerenciador de Tarefas]
    
    - Tarefa existente: {meus_dados}

''')
    
def remover_tarefas():
    tarefa_chave = input('Digite o titulo que deseja excluir -->')
    remover_dado = meus_dados.pop(tarefa_chave, None)

    if remover_dado is not None:
        print(f'''[Gerenciador de Tarefas]
          - Tarefa removida com sucesso.
          - Tarefa exluida --> {remover_dado}''')
    else:
        print(f'''[Gerenciador de Tarefas]
          - Tarefa {tarefa_chave} inexistente.''')
gerenciador_tarefas()

