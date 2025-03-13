Algoritmo partesDeComputadora
    Definir partes Como Cadenas
    Definir parte Como Cadena
    Definir i, j, k Como Entero
    Definir temp Como Cadena
    Dimension partes[100]
    i <- 1
	
    Escribir "Ingrese el nombre de una parte de la computadora (o vacío para terminar):"
    Leer parte
	
    Mientras parte <> "" Hacer
        partes[i] <- parte
        i <- i + 1
        Escribir "Ingrese el nombre de otra parte de la computadora (o vacío para terminar):"
        Leer parte
    FinMientras
	
    Para j <- 1 Hasta i - 2 Hacer
        Para k <- 1 Hasta i - j - 1 Hacer
            Si partes[k] > partes[k + 1] Entonces 
                temp <- partes[k] 
                partes[k] <- partes[k + 1] 
                partes[k + 1] <- temp 
            FinSi
        FinPara
    FinPara
	
    Escribir "Partes de la computadora ordenadas:"
    Para j <- 1 Hasta i - 1 Hacer
        Escribir partes[j]
    FinPara
FinAlgoritmo
