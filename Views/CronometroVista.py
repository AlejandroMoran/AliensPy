import pygame
import sys
from Models.CronometroModelo import CronometroModelo  # importa la clase CronometroModelo definida en CronometroModelo.py


class CronometroVista:
    # Constructor de la clase CronometroVista que carga la fuente para el cronometro.
    def __init__(self):
        self.fuente = pygame.font.SysFont('Comic Sans MS', 40)

    # Método que dibuja la imagen del radar en la pantalla y la posición actual del robot como un blip en el radar.
    def dibujar(self, pantalla, modelo):
        texto = self.fuente.render(f'{modelo.tiempoVivo}', True, (255,255,0))
        area = texto.get_rect()
        area.topright = (pantalla.get_size()[0]-10,10)
        pantalla.blit(texto, area)
