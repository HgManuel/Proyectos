Algoritmo arregloDeFactorial
    Definir n, i Como Entero
    Definir factorial Como Entero
	Dimension factoriales[100] 
	
	
    Escribir "Ingrese un número entero positivo:"
    Leer n
	
    factorial <- 1
    Para i <- 1 Hasta n Hacer
        factorial <- factorial * i
        factoriales[i] <- factorial
    FinPara
	
    Escribir "El factorial de ", n, " es: ", factoriales[n]
	
    Escribir "Factoriales calculados hasta ", n, ":"
    Para i <- 1 Hasta n Hacer
        Escribir "Factorial de ", i, ": ", factoriales[i]
    FinPara
FinAlgoritmo