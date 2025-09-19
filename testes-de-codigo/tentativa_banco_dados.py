banco_dados = {
    'nome_1' : {
        'nome':'Carlos',
        'idade':'21',
        'data-nascimento': '29-09-03',
        'Se alistou?': 'Sim'
    }
}

def selecionar_pessoa():
    selecionar = int(input(f'''
    [nome 1]

'''))
    if selecionar == 1:
        usuario = 'nome_1'
    else:
        print('Opção invalida...')
    print(f'\nVocê solicitou o {usuario}, os dados a seguir do usuario:\n')
    for nome1, nome2 in banco_dados[usuario].items():
        print(f'- {nome1} : {nome2}')
selecionar_pessoa()
