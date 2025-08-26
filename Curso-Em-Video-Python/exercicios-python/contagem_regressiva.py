from time import sleep

print('=#='*5+' CONTAGEM REGRESSIVA '+'=#='*5)

#Carregando a contagem
print('...')
sleep(2)

#Dentro da estrutura for de 10 a 0, com uma pausa de 1 segundo
for contador in range(10,-1,-1):
    print(contador)
    sleep(1)
    
#fim do codigo
print('BOOM!!')