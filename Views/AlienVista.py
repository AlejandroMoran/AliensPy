import pygame


class AlienVista:
    # constructor, recibe una ruta de imagen como argumento
    def __init__(self, ruta_imagen):
        self.imagen = pygame.image.load(ruta_imagen)  # carga la imagen en memoria
        self.imagen.set_colorkey((0, 0, 0))

    # método para dibujar la imagen en la pantalla, recibe la pantalla y el modelo como argumentos
    def dibujar(self, pantalla, modelo):
        area = pygame.Rect(modelo.frame * 32, 0, 32, 32)  # crea un rectángulo para definir el área de la imagen a dibujar, basado en el frame actual del modelo
        pantalla.blit(self.imagen, (modelo.x, modelo.y), area)  # dibuja la imagen en la pantalla en la posición del modelo y la región definida por el rectángulo "area"
