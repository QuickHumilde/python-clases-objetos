#Crear una clase fecha con los siguientes atributos:
#a) int dia,mes,año: Todos ellos privados.
#Los métodos públicos:
#b) ModificarFecha
#c) ModificarDia, ModificarMes, ModificarAño
#d) DevoverDia,DevolverMes,DevolverAño
#e) toString

#Un método privado, que se llama al modificar:
#f) ComprobarFecha: Que hace una comprobación simple:
#1<dia<31 ; 1<mes<12: Si la fecha no es correcta se da un error y no
#se cambia la fecha

class Fecha():
    def __init__(self) -> None:
        self.__dia = 0
        self.__mes = 0
        self.__año = 0
    def modificar_dia(self, dia):
        Fecha.__comprobar_dia(dia)
        self.__dia = dia

    def modificar_mes(self, mes):
        Fecha.__comprobar_mes(mes)
        self.__mes = mes

    def modificar_año(self, año):
        self.__año = año

    def modificar_fecha(self, dia, mes, año):
        self.__comprobar_fecha(dia, mes)
        self.__dia = dia
        self.__mes = mes
        self.__año = año

    def __comprobar_fecha(self, dia, mes):
        Fecha.__comprobar_dia(dia)
        Fecha.__comprobar_mes(mes)
    
    def __comprobar_dia(dia):
        if dia >1 and dia <31:
            return True
        else:
            raise ValueError('El numero debe estar entre 1 y 31')
        
    def __comprobar_mes(mes):
        if mes >1 and mes <12:
            return True
        else:
            raise ValueError('El numero debe estar entre 1 y 12')
        
    def devolver_dia(self):
        return self.__dia

    def devolver_dia(self):
        return self.__dia
    
    def devolver_mes(self):
        return self.__mes

    def devolver_año(self):
        return self.__año
    
    def __str__(self) -> str:
        return str(self.__dia) + "-" + str(self.__mes) + "-" + str(self.__año)

f1 = Fecha()
f1.modificar_fecha(12, 2, 2024)
print(f1)
