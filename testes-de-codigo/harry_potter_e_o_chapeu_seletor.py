grifinoria = 0
corvinal = 0
lufa_lufa = 0
sonserina = 0

print('''
=============================
        HARRY POTTER
=============================

        Chapéu Seletor

''')

question_1 = int(input('''
Q1) Do you like Dawn or Dusk?(Você prefere o amanhecer ou o entardecer?)

  1) Dawn (Amanhecer)
  2) Dusk (Entardecer)

>>> '''))
if question_1 == 1:
  grifinoria += 1
  corvinal += 1
elif question_1 == 2:
  lufa_lufa += 1
  sonserina += 1
else:
  print('Entrada incorreta, tente novamente.')

question_2 = int(input('''
Q2) When I’m dead, I want people to remember me as:
(Quando eu morrer, quero que as pessoas se lembrem de mim como:)

  1) The Good (O Bom)
  2) The Great (O Grande)
  3) The Wise (O Sábio)
  4) The Bold (O Ousado)

>>> '''))

if question_2 == 1:
  lufa_lufa += 2
elif question_2 == 2:
  sonserina += 2
elif question_2 == 3:
  corvinal += 2
elif question_2 == 4:
  grifinoria += 2
else:
  print('Entrada incorreta, tente novamente.')

question_3 = int(input('''
Q3) Which kind of instrument most pleases your ear?
(Qual instrumento musical mais lhe agrada?)

  1) The violin (O violino)
  2) The trumpet (O trompete)
  3) The piano (O piano)
  4) The drum (A bateria)

>>> '''))

if question_3 == 1:
  sonserina += 4
elif question_3 == 2:
  lufa_lufa += 4
elif question_3 == 3:
  corvinal += 4
elif question_3 == 4:
  grifinoria += 4
else:
  print('Entrada incorreta, tente novamente.')

print(f'''
----------------------------------
PONTUAÇÃO TOTAL DE CADA CASA BRUXA
----------------------------------

(1) Grifinoria = {grifinoria} pontos.
(2) Corvinal = {corvinal} pontos.
(3) Lufa-Lufa = {lufa_lufa} pontos.
(4) Sonserina = {sonserina} pontos.


''')
