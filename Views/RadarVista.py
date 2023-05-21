import pygame
from Models.RobotModelo import RobotModelo  # importa la clase RobotModelo definida en RobotModelo.py


class RadarVista:
    # Constructor de la clase RadarVista que carga las imágenes delradar y del blip.
    def __init__(self, imagen_radar, imagen_blip):
        self.imagen_radar = pygame.image.load(imagen_radar)
        self.imagen_blip = pygame.image.load(imagen_blip)

    # Método que dibuja la imagen del radar en la pantalla y la posición actual del robot como un blip en el radar.
    def dibujar(self, pantalla, modelo, Aliens):
        pantalla.blit(self.imagen_radar, (0, 0))
        for a in Aliens:
            pygame.draw.rect(pantalla, (255,0,0), (pygame.Rect((a.modelo.get_posicion()[0]/10)+1, (a.modelo.get_posicion()[1]/10)+1, 3, 3)))
        x = (modelo.x / 10.0) + 1  # convierte la posición x del robot a una posición en el radar
        y = (modelo.y / 10.0) + 1  # convierte la posición y del robot a una posición en el radar
        pantalla.blit(self.imagen_blip, (x, y))
