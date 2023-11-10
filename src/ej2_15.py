"""
Ejercicio 2.1.5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

"""
from ej2_11 import pedirEdad, mayorEdad

def ingresosSup (ingreso, limite) -> bool:
    if ingreso >= limite:
        return True
    else:
        return False


def main():
    edad = pedirEdad()
    limite = 1000
    ingreso = int (input("Introduzca sus ingresos menusales: "))


    if mayorEdad (edad+2) & ingresosSup(ingreso, limite):
        print ("Debe tributar debido a su edad e ingresos mensuales")
    else:
        print ("No cumple los requisitos para tributar")

if __name__ == "__main__":
    main()