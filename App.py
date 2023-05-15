# Importamos los módulos necesarios para el juego
import pygame, os, sys
# Importamos los modelos, vistas y controladores creados para el juego
from RobotModelo import RobotModelo
from RobotVista import RobotVista
from RobotControlador import RobotControlador
from RadarVista import RadarVista
# Inicializamos Pygame
pygame.init()
# Establecemos las dimensiones de la pantalla del juego
pantalla=pygame.display.set_mode((640,480))
# Creamos un reloj para que el juego se ejecute a 30 fps
reloj=pygame.time.Clock()
# Creamos el modelo, la vista y el controlador del robot
robot_modelo=RobotModelo((640-32)/2,(480-32)/2,200)
robot_vista=RobotVista('robotframes.png')
robot_controlador=RobotControlador()
# Creamos la vista del radar
radar_vista=RadarVista('radar.png','blip.png')
# Bucle principal del juego
while True:
    # Detectamos los eventos de Pygame
    for evento in pygame.event.get():
    # Si el evento es del tipo QUIT, salimos del juego y cerramos Pygame y el sistema operativo
    if evento.type==pygame.QUIT:
    pygame.quit()
    sys.exit()

    # Actualizamos el modelo del robot con el tiempo transcurrido y las teclas presionadas
    robot_controlador.actualizar(reloj.get_time(), robot_modelo)

    # Limpiamos la pantalla
    pantalla.fill((0,0,0))
    # Dibujamos la vista del robot y la vista del radar en la pantalla
    robot_vista.dibujar(pantalla,robot_modelo)
    radar_vista.dibujar(pantalla,robot_modelo)

    # Actualizamos la pantalla
    pygame.display.update()
    # Ajustamos la tasa de refresco máxima de 30 fotogramas por segundo para la ventana del juego
    reloj.tick(30)
