"""
Ejercicio 2.1.6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""
def esLetraAnterior (letra_a, letra_b) -> bool:
    return letra_a < letra_b


def perteneceGrupo (sexo, nombre) -> str:
    inicialNombre = nombre[0].upper()

    if (sexo == 'mujer' and esLetraAnterior (inicialNombre,'M')) or \
        (sexo == 'hombre' and esLetraAnterior ('N',inicialNombre)):
        return 'A'
    
    return 'B'

def main():

    nombre = str(input("Introduce tu nombre: "))
    sexo = str(input("Introduce tu sexo (mujer/hombre): "))

    print ("Usted pertenece al grupo: ", perteneceGrupo(sexo, nombre))

if __name__ == "__main__":
    main()