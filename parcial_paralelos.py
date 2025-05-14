# Escriba una funcion que reciba dos vectores y devuelva si son paralelos.

def son_paralelos(vector1, vector2):

    if len(vector1) != len(vector2):
        return None  

    if all(v == 0 for v in vector1) or all(v == 0 for v in vector2):
        return None

    factor = None
    for i in range(len(vector1)):
        if vector1[i] != 0:
            factor = vector2[i] / vector1[i]
            break

    for i in range(len(vector1)):
        if vector1[i] * factor != vector2[i]:
            return False

    return True

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

if __name__ == '__main__':
    print("Primer vector")
    vector_a = ingresar_vector()
    print("Primer vector")
    vector_b = ingresar_vector()

    resultado = son_paralelos(vector_a, vector_b)

    if resultado is None:
        print("No se puede determinar si los vectores son paralelos. Asegúrese de que tengan la misma longitud y que ninguno sea el vector cero.")
    elif resultado:
        print("Los vectores son paralelos.")
    else:
        print("Los vectores no son paralelos.")