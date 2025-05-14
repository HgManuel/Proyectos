# Escribir una funcion que reciba un vector y devuelva su norma.

import math

def norma_vector(vector):

    suma_cuadrados = sum(x**2 for x in vector)
    norma = math.sqrt(suma_cuadrados)
    return norma

def ingresar_vector():
    
    vector = []
    n = int(input("Ingrese la longitud del vector: "))
    for i in range(n):
        while True:
            try:
                elemento = float(input(f"Ingrese el elemento {i + 1}: "))
                vector.append(elemento)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    return vector

if __name__ == "__main__":
    print("Ingrese los elementos del vector")
    mi_vector = ingresar_vector()
    norma = norma_vector(mi_vector)
    print("La norma del vector es:", norma)