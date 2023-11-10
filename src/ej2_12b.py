"""
Ejercicio 2.1.2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""

from ej2_12a import comparaContrasena


def main2 ():
    passw1 = 'Contrasena'

    passw2 = input ("Introduzca la contraseña: ")

    if comparaContrasena (passw1, passw2):
        print ("Contraseña correcta")
    else:
        print ("Contraseña incorrecta")
        main2()

if __name__ == "__main__":
    main2()