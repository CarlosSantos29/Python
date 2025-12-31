from time import sleep
print('''
________________________________
|                              |
|    BEM-VINDO  AO PARQUE SP   |
|  EXPLORE E APROVEITE BEM !!! |
|______________________________|

''')

height = float(input('Digite sua altura (m):'))
sleep(1)
credits = int(input('Quantos de créditos tem disponivel? '))
sleep(1)

if height >= 1.37 and credits >= 10:
  print('Aproveitem a viagem!')
elif height < 1.37:
  print('Você não tem altura suficiente para andar.')
elif credits < 10:
  print('Você não tem creditos suficientes.')
else:
  print('O usuário não atende nenhum dos requisitos.')

sleep(2)
print('''
________________________________
|                              |
|    FIM DA EXECUÇÃO DO CODIGO |
|         OBRIGADO !!!         |
|______________________________|
''')