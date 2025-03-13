Algoritmo barco
	Escribir "Este es el barco construido"
	
	Esperar 200 Milisegundos
	Dimension barco[5]
	
	barco[1] <- "           -----    -----    -----          "
	barco[2] <- "          |     |  |     |  |     |         "
	barco[3] <- "  --------       --       --       -------- "
	barco[4] <- "   \                                     /  "
	barco[5] <- "     \__________________________________/   "
	
	Para i <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir barco[i]
	Fin Para
FinAlgoritmo
