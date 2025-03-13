Algoritmo nmrsElevados
	//Crear un arreglo con n numeros, ingresados por teclado y mostrar sus valores elevados al cuadrado.
	Definir n, i Como Entero
	definir nmrs Como Real
	Dimension nmrs[10]
	
	Escribir "Ingrese la cantidad de numeros:"
	Leer n
		Para i <- 1 Hasta n Con Paso 1 Hacer
			Escribir "ingrese el numero ", i, ": "
			Leer nmrs[i]
		FinPara
		
		Escribir "Los valores de los numeros ingresados elevados al cuadrado son:"
		Para i <- 1 Hasta n con paso 1 Hacer
			Escribir nmrs[i], " elevado al cuadrado es ", nmrs[i] ^ 2
		FinPara
FinAlgoritmo