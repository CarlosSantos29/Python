import pygame

pygame.mixer.init()
pygame.mixer.music.load('/home/carlos/Documentos/Python-Developer-Vscode-Curso-Dio/yonlu.mp3')
pygame.mixer.music.play(-1)

sound_effect = pygame.mixer.Sound('/home/carlos/Documentos/Python-Developer-Vscode-Curso-Dio/yonlu.mp3')

sound_effect.play()

input()
pygame.event.wait()
