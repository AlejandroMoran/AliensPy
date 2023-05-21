import csv
from Models.PuntuacionModelo import PuntuacionModelo
class PuntuacionControlador:
    def __init__(self, archivo):
        self.puntuaciones = []
        self.archivo = archivo
        with open(archivo, newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            for fila in lector_csv:
                self.puntuaciones.append(PuntuacionModelo(fila[0],fila[1]))
            archivo_csv.close()
    def CalcularPuntuacion(self, nuevaPuntuacion):
        for puntuacion in self.puntuaciones:
            if nuevaPuntuacion.tiempoVivo > int(puntuacion.tiempoVivo):
                return True
        return False
    def EscribirPuntuacion(self, nuevaPuntuacion):
        for i in range(len(self.puntuaciones)):
            if nuevaPuntuacion.tiempoVivo > int(self.puntuaciones[i].tiempoVivo):
                if i<2:
                    self.puntuaciones[i+1:] = self.puntuaciones[i:len(self.puntuaciones)-1]
                self.puntuaciones[i] = nuevaPuntuacion
                break
        with open(self.archivo, mode='w', newline='') as archivo_csv:
            fieldnames = ['nombre', 'puntos']
            writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
            for puntuacion in self.puntuaciones:
                registro={'nombre':puntuacion.nombre, 'puntos':puntuacion.tiempoVivo}
                writer.writerow(registro)
            archivo_csv.close()
