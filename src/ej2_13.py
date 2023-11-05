"""
Ejercicio 2.1.3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

def division (num1, num2) -> float:
    return num1 / num2


def main ():
    num1 = int(input("Introduce el dividendo: "))
    num2 = int(input("Introduce el divisor: "))

    if num2 != 0:
        print ('El resultado es: {:,.2f}'.format(division(num1, num2)))
    else:
        print ("**ERROR** El divisor es 0, introduzca otra división")
        main()


if __name__ == "__main__":
    main()