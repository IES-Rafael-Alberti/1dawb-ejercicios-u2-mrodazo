"""
Ejercicio 2.1.7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Menos de 10000€	--> 5%
Entre 10000€ y 20000€ --> 15%
Entre 20000€ y 35000€ --> 20%
Entre 35000€ y 60000€ --> 30%
Más de 60000€ --> 45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

Por mi parte: programado para aceptar números con formato español, inglés o sin nada de nada

"""       
def comprobarNumeric (entrada: str):
    if (entrada.count(".") != 0) or (entrada.count(",") != 0):
        return entrada.replace(".", "").replace(",", "").isnumeric()
    else: 
        return entrada.isnumeric()


def caracterLimitante (entrada: str):
    if entrada.count(".") == 1: #Si hay 1 punto y 1 coma, por defecto el pto es el limitante
        return "."
    elif entrada.count(",") == 1:
        return ","
    else:
        return None

def convertirAFloat (cadena: str) -> float:
    limitante = caracterLimitante(cadena)

    if limitante == None:
        #Si es un entero que lo pase a float
        if (cadena.count(",") == 0) and (cadena.count(".") == 0):
            return float(cadena)
        return None
    
    else:
        #Si el limitante es el ".", las "," sobran
        if limitante == ".": 
            return float(cadena.replace(",", ""))
        #Si la "," es la limitante, hay que cambiarla por un "." y los "." quitarlos
        elif limitante == ",":
            #Si es la ",", quitamos los "." y se cambia la "," para Python OK decimales
            return float (cadena.replace(".", "").replace(",", ".")) 
        else:
            #Si hay separador de unidades con "." o "," pero no decimales, los quita
            if ((cadena.count(".") >1) and (cadena.count(",")==0)) or (((cadena.count(",") >1) and (cadena.count(".")==0))):
                return float (cadena.replace(".", "").replace(",", ""))
            #Si hay más de 1 "." y 1 "," a la vez, el número está mal
            else: 
                return None

def tipoImpositivo (renta: float):
    if renta <= float (10000):
        return 0.05
    if renta <= float (20000):
        return 0.15
    if renta <= float(35000):
        return 0.20
    if renta <= float(60000):
        return 0.30
    return 0.45


def formatearAPorcentaje (num: float) -> str:
    porcentaje = str(int((num*100)))+'%'
    return porcentaje

def main ():
    renta = str(input("Indique su renta anual: "))

    if comprobarNumeric(renta):
        if convertirAFloat (renta)!= None:
            renta_f = convertirAFloat(renta)
            tipo =  tipoImpositivo(renta_f)  
            print ("El tipo impositivo que le corresponde es: ",formatearAPorcentaje(tipo))
        else:
            print ("**ERROR** Caracteres desconocidos en la renta, revise el formato.")
    else:
        print ("**ERROR** Introduzca la renta de nuevo.")
        main()



if __name__ == "__main__":
    main()