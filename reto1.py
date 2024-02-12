# 1.-Crea un programa calculadora que tenga un menú para seleccionar las diferentes 
# operaciones de suma, resta, multiplicación y división y se ejecute hasta que el usuario decida parar.

if __name__=="__main__":
    def menu():
        opcion=1
        while opcion >=1 and opcion<=4:
                opcion = int(input("1.-SUMA | 2.-RESTA | 3.-MULTIPLICACION | 4-DIVISION | 5.-SALIR: "))

                if opcion == 1:
                    def suma():
                        x = int(input("Dime el num x: "))
                        y = int(input("Dime el num y: "))
                        resultado = x + y
                        print(resultado)
                    suma()

                elif opcion == 2:
                    def resta():
                        x = int(input("Dime el num x: "))
                        y = int(input("Dime el num y: "))
                        resultado = x - y
                        print(resultado)
                    resta()

                elif opcion == 3:
                    def multiplicacion():
                        x = int(input("Dime el num x: "))
                        y = int(input("Dime el num y: "))
                        resultado = x * y
                        print(resultado)
                    multiplicacion()

                elif opcion == 4:
                    def division():
                        x = int(input("Dime el num x: "))
                        y = int(input("Dime el num y: "))
                        resultado = x / y
                        print(resultado)
                    division()
    menu()
