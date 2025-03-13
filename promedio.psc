Algoritmo promedio
	Definir cal1, cal2, cal3 Como Real
	Definir prom, notaDefinitiva como real 
	
	Escribir "Ingrese la primera nota:"
	Leer cal1
	Escribir "Ingrese la segunda nota:"
	Leer cal2
	Escribir "Ingrese la tercera nota:"
	Leer cal3
	prom= (cal1 + cal2 + cal3) / 3
	notaDefinitiva= (cal1 + cal2 + cal3) / 3
	
	SI prom >= 4.0 entonces
		Escribir "El estudiante ha aprobado"
	sino Escribir "El estudiante ha reprobado"
	FinSi
	Escribir "La nota definitiva del estudiante es:", notaDefinitiva
	
FinAlgoritmo
