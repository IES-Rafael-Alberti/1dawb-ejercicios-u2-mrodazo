"""
Ejercicio 2.1.2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""

def comparaContrasena(passw1, passw2) -> bool:
    return passw1.lower() == passw2.lower()


def main ():
    passw1 = 'Contrasena'
    intento = True

    while intento:
        passw2 = input ("Introduzca la contraseña: ")
 
        if comparaContrasena (passw1, passw2):
           print ("Contraseña correcta")
           intento = False
        else:
            print ("Contraseña incorrecta")


if __name__ == "__main__":
    main()