"""
Ejercicio 2.1.4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

"""

def parImpar (num) -> str:
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'


def main ():
    num = int (input("Introduce un número: "))
    print ("El número introducido es: " + parImpar(num))



if __name__ == "__main__":
    main()