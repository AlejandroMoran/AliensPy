import pygame


class RobotControlador:
    def actualizar(self, delta_tiempo, modelo):
        # Actualiza el reloj del modelo
        modelo.temporizador -= delta_tiempo
        # Si el tiempo del reloj se acaba, cambia el frame y reinicia el reloj
        if modelo.temporizador < 0:
            modelo.temporizador += modelo.tiempo_reiniciador_temporizador
            modelo.frame += 1
            modelo.frame %= 2

        # Obtiene el estado actual de las teclas presionadas
        teclas = pygame.key.get_pressed()

        # Mueve el modelo según las teclas presionadas
        if teclas[pygame.K_RIGHT]:
            modelo.x += int(modelo.pixelporseg*(delta_tiempo/1000))
        elif teclas[pygame.K_LEFT]:
            modelo.x -= int(modelo.pixelporseg*(delta_tiempo/1000))
        elif teclas[pygame.K_UP]:
            modelo.y -= int(modelo.pixelporseg*(delta_tiempo/1000))
        elif teclas[pygame.K_DOWN]:
            modelo.y += int(modelo.pixelporseg*(delta_tiempo/1000))

        # Limita el movimiento del modelo dentro de la pantalla
        if modelo.x <= 0:
            modelo.x = 0
        if modelo.y <= 0:
            modelo.y = 0
        if modelo.x >= 640-32:
            modelo.x = 640-32
        if modelo.y >= 480-32:
            modelo.y = 480-32
