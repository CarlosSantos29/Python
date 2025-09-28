#dicionario parte 1

#criando dicionario, usando {}
pessoa = {
    'nome': 'Carlos',
    'idade': 22
}
print(pessoa)

pessoa = dict(nome = 'Carlos', idade= 22)
print(pessoa)

pessoa['telefone'] = '4002-8922'
print(pessoa)

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

pessoa['nome'] = 'eduardo'
pessoa['idade'] = 21
pessoa['telefone'] = '4002-8922'

print(pessoa)

contatos = {
    'guilherme@gmail.com':{'nome':'Guilherme', 'telefone': '3333-2221'},
    'giovana@gmail.com':{'nome':'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com':{'nome':'Chappie', 'telefone': '3344-9871'},
    'melaine@gmail.com':{'nome':'Melaine', 'telefone': '3333-7766', 'extra': {'a': 1}}
}
print(contatos['chappie@gmail.com']['telefone'])

extra = contatos['melaine@gmail.com']['extra']['a']
print(extra)

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)