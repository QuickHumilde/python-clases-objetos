# 2.-Crea una nueva versión del programa anterior en el que su modo de ejecución sea 
# que la persona que ejecuta el programa pasa como argumentos la operación a 
# realizar y los operandos. Ejemplo: "python calculadora.py resta 3 2" Debe devolver "3 -2 = 1"

import sys

if __name__=="__main__":
    def menu():
        argumentos = sys.argv

        operacion = argumentos[1]
        num1 = int(argumentos[2])
        num2 = int(argumentos[3])

        if operacion == "suma":
            def suma():
                resultado = num1 + num2
                print(resultado)
            suma()

        elif operacion == "resta":
            def resta():
                resultado = num1 - num2
                print(resultado)
            resta()

        elif operacion == "multiplicacion":
            def multiplicacion():
                resultado = num1 * num2
                print(resultado)
            multiplicacion()

        elif operacion == "division":
            def division():
                resultado = num1 / num2
                print(resultado)
            division()
    menu()
