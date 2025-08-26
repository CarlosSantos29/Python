'''frase_qualquer = str(input('Informe algo: '))
VOGAIS = 'AEIOU'

for contador in frase_qualquer:
    if contador.upper() in VOGAIS:
        print(contador, end='')
else:      
    print()
    print('Executa no final do laço.')'''
    
for contador in range(0, 91, 9):
    print(contador, end =' \n')
    
for contador in range(100):
    '''if contador == 10:
        break
    
    print(contador, end='\n')'''
    
    if contador == 10:
        continue
    
    print(contador, end=' ')