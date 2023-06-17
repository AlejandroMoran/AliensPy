# Importamos los módulos necesarios para el juego
import pygame
import sys
import os
import random
import threading
# Importamos los modelos, vistas y controladores creados para el juego
from Models.PuntuacionModelo import PuntuacionModelo
from Models.RobotModelo import RobotModelo
from Models.CronometroModelo import CronometroModelo
from Models.AlienModelo import AlienModelo
from Models.LetrasModelo import LetrasModelo
from Views.RobotVista import RobotVista
from Views.RadarVista import RadarVista
from Views.CronometroVista import CronometroVista
from Views.AlienVista import AlienVista
from Controllers.RobotControlador import RobotControlador
from Controllers.AlienControlador import AlienControlador
from Controllers.PuntuacionControlador import PuntuacionControlador


class alien:
    def __init__(self, modelo, vista, controlador):
        self.modelo = modelo
        self.vista = vista
        self.controlador = controlador


def pixelArt(palabra):
    global Letras
    Letras = []
    global Aliens
    palabra = palabra.upper()
    palabra = [*palabra]
    for i in range(len(palabra)):
        for pos in letras_modelo.letras[palabra[i]]:
            Letras.append(((pos[0]*32)+(128*i), pos[1]*32))
    for i in range(len(Letras)):
        if i > len(Aliens)-1:
            Ali = generarAlien()
            Ali.modelo.rango = 10000
            Ali.modelo.pixelporseg = 130
            Aliens.append(Ali)
        else:
            Aliens[i].modelo.rango = 10000
            Aliens[i].modelo.pixelporseg = 130
    Aliens = Aliens[:len(Letras)]


# Chechar colisiones
def crash():
    # Comprobamos si hubieron colisiones
    areaAliens = []
    for a in Aliens:
        areaAliens.append(pygame.Rect(a.modelo.get_posicion()[0], a.modelo.get_posicion()[1], 32, 32))
    areaRobot = pygame.Rect(robot_modelo.get_posicion()[0], robot_modelo.get_posicion()[1], 32, 32)
    i = areaRobot.collidelist(areaAliens)
    return i >= 0


# Agregar un alien
def generarAlien():
    # Creamos el controlador y la vista del alien
    alien_vista = AlienVista(os.path.join(dir, 'Media/Images/alien.png'))
    alien_controlador = AlienControlador()
    # Creamos el modelo del alien
    x = random.randint(0, 640-32)
    y = random.randint(0, 480-32)
    while(alien_controlador.calcularDistancia((robot_modelo.x+16, robot_modelo.y+16), (x, y)) < 100):
        x = random.randint(0, 640-32)
        y = random.randint(0, 480-32)
    alien_modelo = AlienModelo(x, y, 0, 200)
    return alien(alien_modelo, alien_vista, alien_controlador)


def cargarPuntos():
    global textos_salon, puntos_controlador
    puntos_controlador = PuntuacionControlador('https://inconclusive-quiet-bittersweet.glitch.me/')
    textoPrimero = font.render(f'1. {puntos_controlador.puntuaciones[0].nombre}', True, (255, 215, 0))
    textoPrimero_area = textoPrimero.get_rect()
    textoPrimero_area.center = (640/2, 200)
    textoSegundo = font.render(f'2. {puntos_controlador.puntuaciones[1].nombre}', True, (192, 192, 192))
    textoSegundo_area = textoSegundo.get_rect()
    textoSegundo_area.center = (640/2, 250)
    textoTercero = font.render(f'3. {puntos_controlador.puntuaciones[2].nombre}', True, (205, 127, 50))
    textoTercero_area = textoTercero.get_rect()
    textoTercero_area.center = (640/2, 300)
    textos_salon = [[textoPrimero, textoPrimero_area], [textoSegundo, textoSegundo_area], [textoTercero, textoTercero_area]]
    reloj.tick(30)
    reloj.tick(30)


t1 = threading.Thread(target=cargarPuntos)
t1.start()
# Obtenemos el directorio de la aplicacion
dir = sys.path[0]
# Inicializamos Pygame
pygame.init()

# Establecemos el nombre de la ventana
pygame.display.set_caption("Aliens")
# Establecemos las dimensiones de la pantalla del juego
pantalla = pygame.display.set_mode((640, 480))
# Creamos un reloj para que el juego se ejecute a 30 fps
reloj = pygame.time.Clock()
# Creamos el modelo, la vista y el controlador del robot
robot_modelo = RobotModelo((640-32)/2, (480-32)/2, 400)
robot_vista = RobotVista(os.path.join(dir, 'Media/Images/robotframes.png'))
robot_controlador = RobotControlador()
# Creamos la vista del radar
radar_vista = RadarVista(os.path.join(dir, 'Media/Images/radar.png'), os.path.join(dir, 'Media/Images/blip.png'))
Aliens = []
# Creamos un evento que sucede cada segundo (1000 ms)
TIMEEVENT = pygame.USEREVENT+1
pygame.time.set_timer(TIMEEVENT, 1000)
# Creamos el contador de segundos del juego:
cronometro_vista = CronometroVista()
cronometro_modelo = CronometroModelo(0)
colision = False

Inicio = True
Juego = False
Fin = False
hs = False
Puntuaciones = False

Letras = []
letras_modelo = LetrasModelo()

font = pygame.font.SysFont('Comic sans', 35)
botonActivo = (100, 100, 100)
botonNormal = (170, 170, 170)

botonJugar = pygame.Rect(0, 0, 250, 38)
botonJugar.center = (640/2, 300)
textoJugar = font.render('Jugar', True, (255, 255, 255))
textoJugar_area = textoJugar.get_rect()
textoJugar_area.center = (640/2, 300)

botonSalon = pygame.Rect(0, 0, 250, 38)
botonSalon.center = (640/2, 350)
textoSalon = font.render('Salon de la fama', True, (255, 255, 255))
textoSalon_area = textoSalon.get_rect()
textoSalon_area.center = (640/2, 350)

botonRegresar = pygame.Rect(0, 0, 120, 38)
botonRegresar.bottomleft = (0+10, 480-10)
textoRegresar = font.render('Regresar', True, (255, 255, 255))
textoRegresar_area = textoRegresar.get_rect()
textoRegresar_area.center = botonRegresar.center

botonMenu = pygame.Rect(0, 0, 250, 38)
botonMenu.center = (640/2, 400)
textoMenu = font.render('Volver al menu', True, (255, 255, 255))
textoMenu_area = textoMenu.get_rect()
textoMenu_area.center = (640/2, 400)

botonEnviar = pygame.Rect(0, 0, 250, 38)
botonEnviar.center = (640/2, 345)
textoEnviar = font.render('Enviar', True, (255, 255, 255))
textoEnviar_area = textoEnviar.get_rect()
textoEnviar_area.center = (640/2, 345)

inputRec = pygame.Rect(0, 0, 180, 28)
inputRec.center = (640/2, 300)
puntos = PuntuacionModelo("", 0)

textoIngresa = font.render('Ingresa tu nombre:', True, (255, 255, 255))
textoIngresa_area = textoIngresa.get_rect()
textoIngresa_area.topright = (inputRec.left-2, inputRec.top+2)

while True:
    if Inicio:
        pixelArt("ALIEN")
        # Detectamos los eventos de Pygame
        for evento in pygame.event.get():
            # Si el evento es del tipo QUIT, salimos del juego y cerramos Pygame y el sistema operativo
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonJugar.collidepoint(mouse):
                    Inicio = False
                    Juego = True
                    Aliens = []
                    Aliens.append(generarAlien())
                elif botonSalon.collidepoint(mouse):
                    Inicio = False
                    Puntuaciones = True
        # Se obtiene la posicion del mouse
        mouse = pygame.mouse.get_pos()

        # Si el usuario pasa el mouse por encima del botonJugar se cambia de color el boton
        if botonJugar.collidepoint(mouse):
            botonJugarColor = botonActivo
        else:
            botonJugarColor = botonNormal

        # Si el usuario pasa el mouse por encima del botonSalon se cambia de color el boton
        if botonSalon.collidepoint(mouse):
            botonSalonColor = botonActivo
        else:
            botonSalonColor = botonNormal

        for i in range(len(Aliens)):
            Aliens[i].controlador.actualizar(reloj.get_time(), Aliens[i].modelo, (Letras[i][0], Letras[i][1]))

        # Limpiamos la pantalla
        pantalla.fill((0, 0, 0))
        pygame.draw.rect(pantalla, botonJugarColor, botonJugar)
        pantalla.blit(textoJugar, textoJugar_area)
        pygame.draw.rect(pantalla, botonSalonColor, botonSalon)
        pantalla.blit(textoSalon, textoSalon_area)
        # Dibujamos la vista de los aliens
        for a in Aliens:
            a.vista.dibujar(pantalla, a.modelo)
        # Actualizamos la pantalla
        pygame.display.update()
        # Ajustamos la tasa de refresco máxima de 30 fotogramas por segundo para la ventana del juego
        reloj.tick(30)

    if Juego:
        # Detectamos los eventos de Pygame
        for evento in pygame.event.get():
            # Si el evento es del tipo QUIT, salimos del juego y cerramos Pygame y el sistema operativo
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == TIMEEVENT:
                cronometro_modelo.tiempoVivo += 1

        # Actualizamos el modelo del robot y de los aliens con el tiempo transcurrido y las teclas presionadas
        robot_controlador.actualizar(reloj.get_time(), robot_modelo)
        for a in Aliens:
            a.controlador.actualizar(reloj.get_time(), a.modelo, (robot_modelo.x, robot_modelo.y))

        # Comprobamos si hubieron colisiones
        colision = crash()
        if colision:
            Juego = False
            Fin = True
            puntos = PuntuacionModelo("", cronometro_modelo.tiempoVivo)
            hs = False

        # Agregamos un alien cada 10 segundos
        if len(Aliens)-1 < int(cronometro_modelo.tiempoVivo/10) and len(Aliens) < 10:
            Aliens.append(generarAlien())

        # Limpiamos la pantalla
        pantalla.fill((0, 0, 0))
        # Dibujamos la vista del robot, la vista de los aliens y la vista del radar y la vista del cronometro en la pantalla
        for a in Aliens:
            a.vista.dibujar(pantalla, a.modelo)
        robot_vista.dibujar(pantalla, robot_modelo)
        radar_vista.dibujar(pantalla, robot_modelo, Aliens)
        cronometro_vista.dibujar(pantalla, cronometro_modelo)
        # Actualizamos la pantalla
        pygame.display.update()
        # Ajustamos la tasa de refresco máxima de 30 fotogramas por segundo para la ventana del juego
        reloj.tick(30)

    if Puntuaciones:
        # Detectamos los eventos de Pygame
        for evento in pygame.event.get():
            # Si el evento es del tipo QUIT, salimos del juego y cerramos Pygame y el sistema operativo
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonRegresar.collidepoint(mouse):
                    Inicio = True
                    Puntuaciones = False
        t1.join()
        # Se obtiene la posicion del mouse
        mouse = pygame.mouse.get_pos()
        if textos_salon[0][1].collidepoint(mouse):
            pixelArt(f"-{int(puntos_controlador.puntuaciones[0].tiempoVivo):03}")
        elif textos_salon[1][1].collidepoint(mouse):
            pixelArt(f"-{int(puntos_controlador.puntuaciones[1].tiempoVivo):03}")
        elif textos_salon[2][1].collidepoint(mouse):
            pixelArt(f"-{int(puntos_controlador.puntuaciones[2].tiempoVivo):03}")
        else:
            pixelArt("-000")

        # Si el usuario pasa el mouse por encima del botonRegresar se cambia de color el boton
        if botonRegresar.collidepoint(mouse):
            botonRegresarColor = botonActivo
        else:
            botonRegresarColor = botonNormal

        for i in range(len(Aliens)):
            Aliens[i].controlador.actualizar(reloj.get_time(), Aliens[i].modelo, (Letras[i][0], Letras[i][1]))

        # Limpiamos la pantalla
        pantalla.fill((0, 0, 0))
        pygame.draw.rect(pantalla, botonRegresarColor, botonRegresar)
        pantalla.blit(textoRegresar, textoRegresar_area)
        pantalla.blit(textos_salon[0][0], textos_salon[0][1])
        pantalla.blit(textos_salon[1][0], textos_salon[1][1])
        pantalla.blit(textos_salon[2][0], textos_salon[2][1])

        # Dibujamos la vista de los aliens
        for a in Aliens:
            a.vista.dibujar(pantalla, a.modelo)
        # Actualizamos la pantalla
        pygame.display.update()
        # Ajustamos la tasa de refresco máxima de 30 fotogramas por segundo para la ventana del juego
        reloj.tick(30)
    if Fin:
        t1.join()
        pantalla.fill((0, 0, 0))
        # Detectamos los eventos de Pygame
        for evento in pygame.event.get():
            # Si el evento es del tipo QUIT, salimos del juego y cerramos Pygame y el sistema operativo
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonMenu.collidepoint(mouse):
                    Inicio = True
                    Fin = False
                    cronometro_modelo.tiempoVivo = 0
                if botonEnviar.collidepoint(mouse):
                    if puntos.nombre != "":
                        puntos_controlador.EscribirPuntuacion(puntos)
                        cargarPuntos()
                        Inicio = True
                        Fin = False
                        cronometro_modelo.tiempoVivo = 0
                    else:
                        puntos.nombre = "Anonimo"
                        puntos_controlador.EscribirPuntuacion(puntos)
                        cargarPuntos()
                        Inicio = True
                        Fin = False
                        cronometro_modelo.tiempoVivo = 0

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    puntos.nombre = puntos.nombre[:-1]
                elif evento.key == pygame.K_RETURN:
                    if puntos.nombre != "":
                        puntos_controlador.EscribirPuntuacion(puntos)
                        cargarPuntos()
                        Inicio = True
                        Fin = False
                        cronometro_modelo.tiempoVivo = 0
                else:
                    puntos.nombre += evento.unicode

        # Se obtiene la posicion del mouse
        mouse = pygame.mouse.get_pos()

        # Si el usuario pasa el mouse por encima del botonJugar se cambia de color el boton
        if botonMenu.collidepoint(mouse):
            botonMenuColor = botonActivo
        else:
            botonMenuColor = botonNormal
        if botonEnviar.collidepoint(mouse):
            botonEnviarColor = botonActivo
        else:
            botonEnviarColor = botonNormal

        if puntos_controlador.CalcularPuntuacion(puntos):
            hs = True
        if hs:
            pixelArt("@")
            for i in range(len(Aliens)):
                Aliens[i].controlador.actualizar(reloj.get_time(), Aliens[i].modelo, (Letras[i][0], Letras[i][1]))
            for a in Aliens:
                a.vista.dibujar(pantalla, a.modelo)
            pygame.draw.rect(pantalla, "White", inputRec)
            nombre = font.render(puntos.nombre, True, (0, 0, 0))
            nombre_area = nombre.get_rect()
            nombre_area.center = inputRec.center
            pantalla.blit(nombre, nombre_area)
            textoNuevaHS = font.render(f'Nuevo record!!!  {cronometro_modelo.tiempoVivo} puntos', True, (255, 255, 255))
            textoNuevaHS_area = textoNuevaHS.get_rect()
            textoNuevaHS_area.center = (640/2, 200)
            pantalla.blit(textoIngresa, textoIngresa_area)
            pantalla.blit(textoNuevaHS, textoNuevaHS_area)
            pygame.draw.rect(pantalla, botonEnviarColor, botonEnviar)
            pantalla.blit(textoEnviar, textoEnviar_area)
        else:
            pixelArt("*")
            for i in range(len(Aliens)):
                Aliens[i].controlador.actualizar(reloj.get_time(), Aliens[i].modelo, (Letras[i][0], Letras[i][1]))
            for a in Aliens:
                a.vista.dibujar(pantalla, a.modelo)
            textoPuntos = font.render(f'Obtuviste {cronometro_modelo.tiempoVivo} puntos', True, (255, 255, 255))
            textoPuntos_area = textoPuntos.get_rect()
            textoPuntos_area.center = (640/2, 200)
            pantalla.blit(textoPuntos, textoPuntos_area)
            pygame.draw.rect(pantalla, botonMenuColor, botonMenu)
            pantalla.blit(textoMenu, textoMenu_area)

        # Actualizamos la pantalla
        pygame.display.update()
        # Ajustamos la tasa de refresco máxima de 30 fotogramas por segundo para la ventana del juego
        reloj.tick(30)
