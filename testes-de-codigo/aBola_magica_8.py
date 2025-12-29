"""
Copia 
Sim, com certeza. x
Com certeza. x 
Sem dúvida. x
Resposta vaga, tente novamente. x
Pergunte novamente mais tarde. x
Melhor não dizer agora. x 
Meus informantes dizem não. x
A perspectiva não é boa. x
Muito improvável. x
"""
from random import randint

print('''
________________________________
|                              |
|     BEM VINDO AO 8 POOL      |
|         DIVIRTA-SE           |
|______________________________|

''')

pergunta_aleatoria = input('''
------------ Testando ------------

Escreva alguma pergunta em mente, que a maquina
te responderá da melhor forma possível.

Digite aqui sua resposta >>>> ''')
numero_gerado = randint(1,9)

if numero_gerado == 1:
  bola_magica_8 = 'Sim, com certeza.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 2:
  bola_magica_8 = 'Com certeza.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 3:
  bola_magica_8 = 'Sem dúvida.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 4:
  bola_magica_8 = 'Resposta vaga, tente novamente.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 5:
  bola_magica_8 = 'Pergunte novamente mais tarde.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 6:
  bola_magica_8 = 'Melhor não dizer agora. '
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 7:
  bola_magica_8 = 'Meus informantes dizem não.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')
elif numero_gerado == 8:
  bola_magica_8 = 'A perspectiva não é boa.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')

else:
  bola_magica_8 = 'Muito improvável.'
  print(f'''
  -------------------------------
  | SOLUÇÃO GERADA PELA MAQUINA |
  -------------------------------
  Pergunta: {pergunta_aleatoria}
  Resposta da Bola Mágica 8: {bola_magica_8} 
  ------------------------------''')

print('''
________________________________
|                              |
|    FIM DA EXECUÇÃO DO CODIGO |
|         OBRIGADO !!!         |
|______________________________|

''')