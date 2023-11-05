"""
Ejercicio 2.1.7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Menos de 10000€	--> 5%
Entre 10000€ y 20000€ --> 15%
Entre 20000€ y 35000€ --> 20%
Entre 35000€ y 60000€ --> 30%
Más de 60000€ --> 45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

"""
def esFloat (entrada:str):
    return entrada.count(".") == 1 and entrada.replace(".", "").isnumeric()
        


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
    porcentaje = str((num*100))+'%'


def main ():
    renta = input("Indique su renta anual: ")
    if esFloat (renta):
        tipo =  tipoImpositivo(float(renta))  
        print ("El tipo impositivo que le corresponde es: ",formatearAPorcentaje(tipo))
    else:
        print ("**ERROR** renta no es un tipo float")



if __name__ == "__main__":
    main()