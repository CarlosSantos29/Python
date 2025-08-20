# parte ira quebra os espaços tranformando em lista.
nome_usuario = input('Digite o nome do usuario que está executando isso: ').strip().split()
print(f'O primeiro nome: {nome_usuario[0]}')  # primeiro nome.
# ultimo nome, notasse que está -1, porque como não tem noção do tamanho de espaço, o ultimo nome não aparece na lista.
print(f'O ultimo nome: {nome_usuario[-1]}')
