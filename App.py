# Importamos los módulos necesarios para el juego
import pygame
import sys
import os
# Importamos los modelos, vistas y controladores creados para el juego
from Models.RobotModelo import RobotModelo
from Views.RobotVista import RobotVista
from Controllers.RobotControlador import RobotControlador
from Views.RadarVista import RadarVista
from Views.CronometroVista import CronometroVista
from Models.CronometroModelo import CronometroModelo

#Obtenemos el directorio de la aplicacion
dir = sys.path[0]
# Inicializamos Pygame
pygame.init()
# Establecemos las dimensiones de la pantalla del juego
pantalla = pygame.display.set_mode((640, 480))
# Creamos un reloj para que el juego se ejecute a 30 fps
reloj = pygame.time.Clock()
# Creamos el modelo, la vista y el controlador del robot
robot_modelo = RobotModelo((640-32)/2, (480-32)/2, 200)
robot_vista = RobotVista(os.path.join(dir, 'Media/Images/robotframes.png'))
robot_controlador = RobotControlador()
# Creamos la vista del radar
radar_vista = RadarVista(os.path.join(dir, 'Media/Images/radar.png'), os.path.join(dir, 'Media/Images/blip.png'))
# Creamos un evento que sucede cada segundo (1000 ms)
TIMEEVENT = pygame.USEREVENT+1
pygame.time.set_timer(TIMEEVENT, 1000)
#Creamos el contador de segundos del juego:

cronometro_vista = CronometroVista()
cronometro_modelo = CronometroModelo(0)
# Bucle principal del juego
while True:
    # Detectamos los eventos de Pygame
    for evento in pygame.event.get():
        # Si el evento es del tipo QUIT, salimos del juego y cerramos Pygame y el sistema operativo
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == TIMEEVENT:
            cronometro_modelo.tiempoVivo += 1


    # Actualizamos el modelo del robot con el tiempo transcurrido y las teclas presionadas
    robot_controlador.actualizar(reloj.get_time(), robot_modelo)

    # Limpiamos la pantalla
    pantalla.fill((0, 0, 0))
    # Dibujamos la vista del robot y la vista del radar en la pantalla
    robot_vista.dibujar(pantalla, robot_modelo)
    radar_vista.dibujar(pantalla, robot_modelo)
    cronometro_vista.dibujar(pantalla, cronometro_modelo)
    # Actualizamos la pantalla
    pygame.display.update()
    # Ajustamos la tasa de refresco máxima de 30 fotogramas por segundo para la ventana del juego
    reloj.tick(30)
