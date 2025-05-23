#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#  El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior
# a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y
# muestre por pantalla el grupo que le corresponde.

nombre = input("ingrese su nombre: ").strip().title()
sexo = input("ingrese su sexo(M para mujer, H para hombre): ").strip().upper()
           
if (sexo == "M" and nombre(0) < "M" ) or (sexo == "H" and nombre[0] > "N"  ):
    grupo = "A"
else:
    grupo = "B"

print("Usted pertenece al grupo: ", grupo)