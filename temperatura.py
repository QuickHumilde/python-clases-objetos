#Crea una clase Temperatura, con los siguiente atributos:
#a) Una fecha (Composición)
#b) Una temperatura máxima y una temperatura mínima.
#Los métodos:
#c) Los constructores
#d) Modificar temperaturas
#e) Devolver temp. max, temp. min. y temp_media
#f) toString: Que debe mostrar en pantalla la fecha, la temp. max., la temp.
#min y la temp. media.

class Temperatura():
    def __init__(self, fecha, tempmax, tempmin):
        self.fecha = fecha
        self.tempmax = tempmax
        self.tempmin = tempmin
    def modificar_temp(self, max_nueva, min_nueva):
        self.__tempmax = max_nueva
        self.__tempmin = min_nueva
    def devolver_max(self):
        return self.tempmax
    def devolver_min(self):
        return self.__tempmin
    def devolver_media(self):
        return ((self.tempmax + self.tempmin)/2)
    
    def __str__(self):
        return f"Fecha: {self.fecha}. Temp min: {self.tempmin}ºC. Temp max: {self.tempmax}ºC. Temp media: {self.devolver_media()}ºC"
    
tempmax = 25
tempmin = 10
fecha = "12-02-2024"
t1 = Temperatura(fecha, tempmax, tempmin)
print(t1)
