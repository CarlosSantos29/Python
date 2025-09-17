from time import sleep
personagens = {
    'Naruto':{
        'Habilidade': 'Rasengan',
        'Jinchuriki': 'Raposa',
        'Susanoo': 'No',
        'Ninjutsu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'Uzumaki'
    },
    'Sasuke':{
        'Habilidade': 'Chidori/Sharingan',
        'Jinchuriki': 'N/A',
        'Susanoo': 'Yes',
        'Ninjutsu': 'Yes',
        'Genjutsu': 'Yes',
        'Taijutsu': 'Yes',
        'Clã': 'Uchiha'
    },
    'Sakura': {
        'Habilidades': 'Técnicas ninja médica',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjutsu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'Haruno'

    },
    'Shikamaru': {
        'Habilidades': 'Manipulação ninja das sombras',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjutsu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'Nara'
    },
    'Ino': {
        'Habilidades': 'Técnicas ninja médica/Telepatia',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjutsu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': ''
    },
    'Choji': {
        'Habilidades': 'Convenção de calórias em chackra',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjutsu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'Akimichi'
    },
    'Rock Lee': {
        'Habilidades': 'Capacidade de abrir os 8 portões internos',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjutsu': 'No',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'Lee'
    },
    'Neji': {
        'Habilidades': 'Byakugan',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjustu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'Hyuga'
    },
    'Tenten': {
        'Habilidades': 'Manipulação de armas ninja',
        'Jinchuriki': 'No',
        'Susanoo': 'No',
        'Ninjustu': 'Yes',
        'Genjutsu': 'No',
        'Taijutsu': 'Yes',
        'Clã': 'N/A'
    }

}
def historico_ninjas():
    escolha_ninja = 0
    while True:
            escolha_ninja = int(input(f'''
    ====== Escolha um ninja e veja suas habilidades ====
                              
           Time 7    Time 10        Time 9     
        [1 NARUTO]  [4 Shikamaru]   [7 Rock Lee]   [10 Sair]
        [2 SASUKE]  [5 Ino]         [8 Neji]
        [3 SAKURA]  [6 Choji]       [9 Tenten]
                              
    escolha aqui seu ninja ---> '''))
            if escolha_ninja == 1:
                ninja = "Naruto"
            elif escolha_ninja == 2:
                ninja = "Sasuke"
            elif escolha_ninja == 3:
                ninja = 'Sakura'
            elif escolha_ninja == 4:
                ninja = 'Shikamaru'
            elif escolha_ninja == 5:
                ninja = 'Ino'
            elif escolha_ninja == 6:
                ninja = 'Choji'
            elif escolha_ninja == 7:
                ninja = 'Rock Lee'
            elif escolha_ninja == 8:
                ninja = 'Neji'
            elif escolha_ninja == 9:
                ninja = 'Tenten'
            elif escolha_ninja == 10:
                saindo_menu()
                break
            else:
                print('Opção invalida.')
                continue
        
    
            print(f'\nVocê escolheu {ninja}\nSobre ele(a):\n')
    
            for chave, valor in personagens[ninja].items():
                print(f'- {chave}: {valor}')
def saindo_menu():
    print('Saindo em...')
    for contador in [3,2,1]:
        print(contador)
        sleep(3)

historico_ninjas()
print('Fim do codigo...')
