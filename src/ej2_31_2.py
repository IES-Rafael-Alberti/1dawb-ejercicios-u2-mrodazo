"""
Ejercicio 2.3.1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

Otra forma (metiendo la excepción fuera) y aparte metiendo el raise
"""

from ej2_213 import borrarConsola

def mostrarSerie(edad: int) -> str: #-> str eso significa que va a devolver un str por fuerza
    serie = ""
    for i in range (1, edad + 1):
        serie += str (i) + " "
    
    return serie


def pedirEdad (msj: str):
    entrada = input (msj)
    edad = int (entrada) #Si esta conversión falla da un ValueError

    if edad <=0:
        raise Exception ("No me gusta esa edad")
    
    return edad

def main ():
    borrarConsola()

    error = True
    while error:
        try:      
            edad = pedirEdad("Introduzca su edad: ")
            error = False
        except ValueError:
            print ("**ERROR** edad no válida.")
        except Exception:
                print ("**ERROR** edad negativa o 0.")
        except:
            print ("**ERROR**")


    print (mostrarSerie(edad))



    if __name__ == "__main__":
        main()