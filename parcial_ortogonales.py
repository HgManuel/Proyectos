# Escriba una funcion que reciba dos vectores y devuelva si son o no ortogonales.

def son_ortogonales(vector1, vector2):
    if len(vector1) != len(vector2):
        return None 

    producto_escalar = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    return producto_escalar == 0

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
    print("Segundo vector")
    vector_b = ingresar_vector()

    resultado = son_ortogonales(vector_a, vector_b)

    if resultado is None:
        print("Los vectores deben tener la misma longitud para verificar la ortogonalidad.")
    elif resultado:
        print("Los vectores son ortogonales.")
    else:
        print("Los vectores no son ortogonales.")