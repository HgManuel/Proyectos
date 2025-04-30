Algoritmo parcial
	//Realizar un algoritmo para determinr cuanto ahorrara una persona en un año, si al final de cada mes deposita cantidades variables de dinero; ademas, se quiere saber cuanto lleva ahorrado cada mes.
	Definir ahorroMensual, ahorroTotal Como Real
	Definir mes Como entero
	
	ahorroTotal <- 0
	
	Escribir "Calcular el ahorro anual"
	Escribir "------------------------"
	
	Para mes <- 1 Hasta 12 Con Paso 1 Hacer
		Escribir "Ingrese la cantidad ahorrada en el mes ", mes, ":"
		Leer ahorroMensual
		
		Mientras ahorroMensual < 0 Hacer 
			Escribir "Ingrese una cantidad valida:"
			Leer ahorroMensual
		FinMientras
		
		ahorroTotal <- ahorroTotal + ahorroMensual
		
		Escribir "Mes ", mes, " - Ahorro acumulado: $", ahorroTotal
		Escribir "---------------------------"
	FinPara
	
	Escribir "Ahorro total del año: $" ahorroTotal
	
	
	
	
	
FinAlgoritmo
