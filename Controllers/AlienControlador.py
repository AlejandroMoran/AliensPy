import math


class AlienControlador:
    def calcularDistancia(self, objetivo, posicion):
        return math.sqrt((objetivo[0]-posicion[0]) ** 2 + (objetivo[1]-posicion[1]) ** 2)

    def actualizar(self, delta_tiempo, modelo, objetivo):
        # Actualiza el reloj del modelo
        modelo.cronometro = modelo.get_cronometro() + delta_tiempo

        # Si el tiempo del reloj se acaba, cambia el frame y reinicia el reloj
        if modelo.get_cronometro() > modelo.get_tiempo_reiniciador_cronometro():
            modelo.siguiente_frame()

        # Limita el movimiento del modelo dentro de la pantalla
        posicion = modelo.get_posicion()
        if posicion[0] <= 0:
            modelo.set_posicion((0, posicion[1]))
            modelo.direccionx = -modelo.direccionx
        if posicion[1] <= 0:
            modelo.set_posicion((posicion[0], 0))
            modelo.direcciony = -modelo.direcciony
        if posicion[0] >= 640-32:
            modelo.set_posicion((640-32, posicion[1]))
            modelo.direccionx = -modelo.direccionx
        if posicion[1] >= 480-32:
            modelo.set_posicion((posicion[0], 480-32))
            modelo.direcciony = -modelo.direcciony

        # Comprueba si hay un enemigo cerca
        distancia = self.calcularDistancia(objetivo, posicion)
        if distancia < modelo.rango:
            modelo.seguir = True
        else:
            modelo.seguir = False

        # Sigue al jugador
        if modelo.seguir:
            if distancia != 0:
                distancia_x, distancia_y = (objetivo[0]-posicion[0])/distancia, (objetivo[1]-posicion[1])/distancia
                modelo.x += distancia_x*modelo.pixelporseg*(delta_tiempo/1000)
                modelo.y += distancia_y*modelo.pixelporseg*(delta_tiempo/1000)
                if distancia < (modelo.pixelporseg*(delta_tiempo/1000)):
                    modelo.x = objetivo[0]
                    modelo.y = objetivo[1]

        if not modelo.seguir:
            modelo.x += modelo.direccionx*(delta_tiempo/1000)
            modelo.y += modelo.direcciony*(delta_tiempo/1000)
