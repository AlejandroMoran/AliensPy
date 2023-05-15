class RobotModelo:
    # Método constructor
    def __init__(self, x, y, tiempo_reiniciador_temporizador):
        self.x = x
        self.y = y
        self.tiempo_reiniciador_temporizador = tiempo_reiniciador_temporizador
        self.frame = 0
        self.temporizador = tiempo_reiniciador_temporizador
        self.pixelporseg = 200
