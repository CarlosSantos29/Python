nome = 'Carlos'
idade = 21
profissão = 'Desenvolvedor'
linguagem = 'Python'
informações = {'profissão': 'Desenvolvedor', 'linguagem': 'Python', 'Salario': 25.045}


print('Nome: %s Idade: %d' %(nome,idade))#Python 2
print('Nome: {} Idade: {}'.format(nome,idade))#Python3
print('Nome: {0} Idade: {1}'.format(nome,idade))
print('Nome: {nome} Idade: {idade}'.format(nome=nome,idade=idade))  
print(f'Nome: {nome} Idade: {idade}')# Python3 F-string
print('Profissão: {profissão} Linguagem: {linguagem}'.format(**informações))
print('Profissão: {profissão} Linguagem: {linguagem} Salario: R${Salario:10.3f}'.format(**informações))