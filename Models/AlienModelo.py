import random
import math


class AlienModelo:
    def __init__(self, x, y, frame, tiempo_reiniciador_cronometro):
        # Inicializa los atributos del objeto
        self.x = x
        self.y = y
        self.tiempo_reiniciador_cronometro = tiempo_reiniciador_cronometro
        self.frame = frame
        self.cronometro = 0
        self.rango = 150
        self.seguir = False
        self.pixelporseg = 75
        self.direccionx = random.randint(0, int(self.pixelporseg/2))
        self.direcciony = math.sqrt((self.pixelporseg/2)**2 - self.direccionx**2)
        if random.randint(0, 1) == 1:
            self.direccionx = -self.direccionx
        if random.randint(0, 1) == 1:
            self.direcciony = -self.direcciony

    def get_posicion(self):
        # Devuelve la posición actual del alien
        return (self.x, self.y)

    def set_posicion(self, nueva_posicion):
        # Establece la posición del alien en una nueva posición
        self.x = nueva_posicion[0]
        self.y = nueva_posicion[1]

    def get_frame(self):
        # Devuelve el número de cuadro actual de la animación del alien
        return self.frame

    def get_cronometro(self):
        # Devuelve el valor actual del cronómetro
        return self.cronometro

    def get_tiempo_reiniciador_cronometro(self):
        # Devuelve el valor del tiempo de reinicio del cronómetro
        return self.tiempo_reiniciador_cronometro

    def set_tiempo_reiniciador_cronometro(self, nuevo_tiempo_reiniciador_cronometro):
        # Establece un nuevo valor para el tiempo de reinicio del cronómetro
        self.tiempo_reiniciador_cronometro = nuevo_tiempo_reiniciador_cronometro

    def siguiente_frame(self):
        # Reinicia el cronómetro y actualiza el número de cuadro de la animación
        self.cronometro = 0
        self.frame += 1
        self.frame %= 4
