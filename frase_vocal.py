#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y 
# después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Introduzca una frase: ")
vocal = input("Introduzca una vocal: ")

if vocal in "aeiouAEIOU" and len(vocal) == 1:
    frase_modificada = frase.replace(vocal, vocal.upper()).replace(vocal.upper(), vocal.upper())
    print("Frase modificada:", frase_modificada)
else:
    print("Por favor, introduzca una sola vocal valida (a, e, i, o, u).")