"""
Ejercicio 2.1.8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel Inaceptable --> Puntuación 0.0
Nivel Aceptable --> Puntuación 0.4
Nivel Meritorio --> Puntuación 0.6 o más

"""
#Comprueba si en el array de valores correctos está la puntuación indicada
def comprobarPuntuacion(puntos):
    return ((puntos == 0.0) or (puntos == 0.4) or (puntos >= 0.6))


def nivel (puntos) -> str:
    if puntos == 0.0:
        return 'Nivel inaceptable'
    elif puntos == 0.4:
        return 'Nivel aceptable'
    elif puntos >= 0.6:
        return 'Nivel meritorio'
    return None

def bonificacion (puntos) -> float:
    return puntos*2400


def main():
    puntos = float (input("Introduzca su puntuación: "))

    if comprobarPuntuacion(puntos) and (nivel(puntos)!= None):
        print (nivel(puntos), 'su bonificación es: {:,.2f}€'.format(bonificacion(puntos))), 
    else:
        print ("La puntuación indicada es errónea, intente de nuevo.")
        main()



if __name__ == "__main__":
    main()