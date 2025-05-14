# Escriba una funcion que reciba dos vectores y devuelva su producto escalar.

def productoEscalar(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    producto = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    return producto

if __name__ == '__main__':
    def input_vector():
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

    print("Primer vector")
    vector_a = input_vector()
    print("Segundo vector")
    vector_b = input_vector()

    resultado = productoEscalar(vector_a, vector_b)
    if resultado is not None:
        print("El producto escalar es:", resultado)
    else:
        print("Los vectores deben tener la misma longitud.")

