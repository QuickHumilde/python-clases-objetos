#Practica de clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

#--------------------------------

class Persona:
    #Le ponemos valores por defecto
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

mi_persona = Persona("Bruno", "Diaz")
print(f"Hola, me llamo {mi_persona.nombre} de apellido {mi_persona.apellido}")


#-----------------------------------

class Persona2:
    #Le ponemos valores por defecto
    def __init__(self, nombre, apellido, alias = "Alias desconocido"):
        self.completo = f"{nombre} {apellido} ({alias})"
        self.__nombre = nombre
        self.__apellido = apellido

    def respirar (self):
        print(f"Increiblemente, {self.completo} está respirando")

mi_persona2 = Persona2("Pedro", "Parker")
print(mi_persona2.completo)
mi_persona2.respirar()

#Aqui, le definimos valores
mi_otra_persona = Persona2("Julio", "Iglesias", "Masón")
print(mi_otra_persona.completo)
mi_otra_persona.respirar()

#Le cambiamos el valor a .completo
mi_otra_persona.completo = "Maria Juana (La atrapa arañas)"
print(mi_otra_persona.completo)

mi_otra_persona.completo = 893508
print(mi_otra_persona.completo)

#------------------------

class Persona3:
    #Le ponemos valores por defecto y ponemos privado los valores de nombre 
    def __init__(self, nombre, apellido, edad, alias = "La mama de la mama"):
        self.completo = f"{nombre} {apellido} {edad} ({alias})"
        self.__nombre = nombre
        self.__edad = edad

    #GETTER DE NOMBRE
    def get_nombre (self):
        print (f"VOY A DAR EL NOMBRE")
        return self.__nombre

    #SETTER DE EDAD
    def set_edad (self, edad):
        if edad >= 0:
            #Si la edad es mayor o igual que 0, perfe
            self.__edad = edad
        else:
            #Si la edad es negativa, no esta permitido
            raise ValueError("La edad no puede ser negativa")

    #DELETTER DE EDAD
    def del_edad (self):
        del self.__edad

    #GETTER DE EDAD
    def get_edad (self):
        print (f"VOY A DAR LA EDAD")
        return self.__edad

mi_persona3 = Persona3("NOMBRE-PRIVADO", "CARACOLA", 4)

#No funciona sin getter
##print(mi_persona3.__nombre)

#Si funciona con getter
print(mi_persona3.get_nombre())

mi_persona3.set_edad(61)

#Si le pongo esto, al intentar hacer el print de __edad me diria que no existe
 #del mi_persona3.__edad

print(mi_persona3.get_edad())

#--------------------------


class Persona4:
    #Le ponemos valores por defecto y ponemos privado los valores de nombre 
    def __init__(self, edad):
        self.__edad = edad

    #SETTER DE EDAD
    def set_edad (self, edad):
        if edad >= 0:
            #Si la edad es mayor o igual que 0, perfe
            self.__edad = edad
        else:
            #Si la edad es negativa, no esta permitido
            raise ValueError("La edad no puede ser negativa")

    #DELETTER DE EDAD
    def del_edad (self):
        del self.__edad

    #GETTER DE EDAD
    def get_edad (self):
        print (f"VOY A DAR LA EDAD")
        return self.__edad

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de edad {1} mientras {2}"
        return msg.format(clase, self.__edad, "llora")

    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})({2})"
        return msg.format(clase, self.__edad, "llora")


mi_persona4 = Persona4(4)

print(mi_persona4)
#   >>Persona4 de edad 4 mientras llora

print(repr(mi_persona4))
#   >>Persona4(4)(llora)
