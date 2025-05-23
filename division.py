#Escribir un programa que pida al usuario dos números y
# muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))

if x / y == 0:
    print("Error, no se puede dividir entre cero")
else:
    print(x/y)