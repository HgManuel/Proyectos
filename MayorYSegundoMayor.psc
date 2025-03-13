Algoritmo MayorYSegundoMayor
		Definir n, i, mayor, segundoMayor Como Entero
		Dimension numeros[100]
		
		Escribir "Ingrese la cantidad de números:"
		Leer n
		
		Para i = 1 Hasta n Hacer
			Escribir "Ingrese el número ", i, ":"
			Leer numeros[i]
		FinPara
		
		Si numeros[1] > numeros[2] Entonces
			mayor = numeros[1]
			segundoMayor = numeros[2]
		SiNo
			mayor = numeros[2]
			segundoMayor = numeros[1]
		FinSi
		
		Para i = 3 Hasta n Hacer
			Si numeros[i] > mayor Entonces
				segundoMayor = mayor
				mayor = numeros[i]
			SiNo
				Si numeros[i] > segundoMayor Y numeros[i] <> mayor Entonces
					segundoMayor = numeros[i]
				FinSi
			FinSi
		FinPara
		
		Escribir "El número mayor es: ", mayor
		Escribir "El segundo número mayor es: ", segundoMayor
FinAlgoritmo
