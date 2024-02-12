#Clase Bombilla
# 1. Crea la clase Bombilla de las transparencias, ahora retoca la clase Bombilla para 
#que cumpla con los siguientes requisitos:

# -Si la bombilla estaba encendida y se vuelve a encender se debe mostrar el
# mensaje “La bombilla ya estaba encendida” y no aumentar el contador de
# número encendidos. 

# -Si la bombilla estaba apagada y se vuelve a apagar se debe mostrar el
# mensaje “La bombilla ya estaba apagada”. 

# -Cuando se produzca el encendido 1000 la bombilla debe fundirse y escribir
# el mensaje “La bombilla se ha fundido”. En este estado, si se intenta
# encender o apagar se debe mostrar el mensaje “La bombilla está fundida”.

class Bombilla:
    def __init__(self):
        self._encendida = False
        self._vecesEncendidas=0

    def encender(self):
        if self.fundida() == True:
            print ("La bombilla esta fundida")
            return
        if self._encendida == True:
            print ("La bombila ya esta encendida")
            return
        self._encendida=True
        self._vecesEncendidas +=1
        if self.fundida():
            print("La bombilla se ha fundido")

    def apagar(self):
        if self.fundida():
            print("La bombilla esta fundida")
            return
        if self._encendida == False:
            print("La bombilla ya estaba encendida")
            return
        self._encendida=False

    def fundida(self):
        return self._vecesEncendidas >= 1000
    
bombilla1 = Bombilla()
for i in range(1000):
    bombilla1.apagar()
    bombilla1.encender()
