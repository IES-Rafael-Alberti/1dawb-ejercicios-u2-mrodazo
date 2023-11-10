"""
Ejercicio 2.3.1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

"""

from ej2_213 import borrarConsola

def mostrarSerie(edad: int) -> str: "-> str eso significa que va a devolver un str por fuerza"
    serie = ""
    for i in range (1, edad + 1):
        serie += str (i) + " "
    
    return serie


def pedirEdad (msj: str):
    
    error = True "Se pone así para que al menos ejecute 1 vez el while"
    while error:
    try:
        edad = int (input (msj))
        error = False "Si metemos un valor correcto, se cambia el valor de error para que no repita el while"
    except:
        print ("**ERROR** Edad no válida.")

    return edad

def main ():
    borrarConsola()

    edad = pedirEdad("Introduzca su edad: ")

    print (mostrarSerie(edad))



    if __name__ == "__main__":
        main()