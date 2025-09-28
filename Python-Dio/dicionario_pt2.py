#dicionarios parte 2


contatos = {
    'guilherme@gmail.com':{'nome':'Guilherme', 'telefone': '3333-2221'},
    'giovana@gmail.com':{'nome':'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com':{'nome':'Chappie', 'telefone': '3344-9871'},
    'melaine@gmail.com':{'nome':'Melaine', 'telefone': '3333-7766', 'extra': {'a': 1}}
}

#contatos.clear()

print(contatos)

contato = {
    'guilherme@gmail.com':{'nome':'Guilherme', 'telefone': '3333-2221'}
}

copia = contatos.copy()
copia['guilherme@gmail.com'] = {'nome':'Gui'}

print('Dicionario Original: ',contatos['guilherme@gmail.com'])
print('Copia do dicionario: ',copia['guilherme@gmail.com'])

print(dict.fromkeys(['nome','telefone']))#cria um dicionario com as chaves passadas
print(dict.fromkeys(['nome','telefone'], 'default'))#cria um dicionario com as chaves passadas e o valor default

contato = {
    'guilherme@gmail.com':{'nome':'Guilherme', 'telefone': '3333-2221'}
}

#print(contatos.get['chave'])#Keyerror
print(contatos.get('chave'))#retorna nada
print(contatos.get('chave', {}) )# retorna um dicionario vazio
print(contatos.get('guilherme@gmail.com', {}))#retorna o valor do dicionario
print(contatos.items())#retorna os itens do dicionario 
print(contatos.keys())#retorna as chaves do dicionario
#print(contatos.pop('guilherme@gmail.com', {}))#remove o item do dicionario e retorna o valor, se não encontrar retorna o valor default
#print(contatos.pop('guilherm#gmail.com', 'Não encontrado :('))#remove o item do dicionario e retorna o valor, se não encontrar retorna o valor default
#print(contatos.popitem())

contato = {'nome': 'Carlos', 'telefone': '4002-8922'}
print(contato.setdefault('nome', 'informação desconhecida.'))
print(contato)
print(contato.setdefault('idade', 21))
print(contato)

contato.update({'guilherme@gmail.com': {'nome':'Gui'}})
print(contato)

contato.update({'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}})
print(contato)


contatos = {
    'guilherme@gmail.com':{'nome':'Guilherme', 'telefone': '3333-2221'},
    'giovana@gmail.com':{'nome':'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com':{'nome':'Chappie', 'telefone': '3344-9871'},
    'melaine@gmail.com':{'nome':'Melaine', 'telefone': '3333-7766', 'extra': {'a': 1}}
}

print(contatos.values())#retorna os valores do dicionario

print('guilherme@gmail.com' in contatos)
print('megui@gmail.com' in contatos)
print('idade' in contatos['guilherme@gmail.com'])
print('telefone' in contatos['giovana@gmail.com'])

del contatos['guilherme@gmail.com']['telefone']
print(contatos)

del contatos['chappie@gmail.com']
print(contatos)

del contatos
print(contatos, {})