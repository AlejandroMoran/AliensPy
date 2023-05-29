import json
import urllib.request
from Models.PuntuacionModelo import PuntuacionModelo
class PuntuacionControlador:
    def __init__(self, archivo):
        self.puntuaciones = []
        self.URL="https://inconclusive-quiet-bittersweet.glitch.me/"
        get = urllib.request.Request(self.URL)
        response = urllib.request.urlopen(get)
        lector = response.read().decode('utf8').split("\n")
        for row in lector:
            fila = row.split(",")
            self.puntuaciones.append(PuntuacionModelo(fila[0],fila[1]))

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
        datos = ""
        for puntuacion in self.puntuaciones:
            datos += f"{puntuacion.nombre},{puntuacion.tiempoVivo}\n"
        datos = datos.strip()

        body = {
            "data" : datos
        }
        post = urllib.request.Request(self.URL)
        post.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        post.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(post, jsondataasbytes)
