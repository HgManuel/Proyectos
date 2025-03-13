Algoritmo GastoViajeTuristico
    Definir destinos Como Cadenas
    Definir distancias, costosGalon Como Reales
    Definir i Como Entero
    Definir gasto, consumo Como Real
	
    Dimension destinos[3]
    Dimension distancias[3]
    Dimension costosGalon[3]
	
    Para i <- 1 Hasta 3 Hacer 
        Escribir "Ingrese el nombre del destino ", i, ":"
        Leer destinos[i]
        Escribir "Ingrese la distancia desde Lima (en km) a ", destinos[i], ":"
        Leer distancias[i]
        Escribir "Ingrese el costo del galón de gasolina a ", destinos[i], ":"
        Leer costosGalon[i]
    FinPara
	
    Para i <- 1 Hasta 3 Hacer 
        consumo <- distancias[i] / 10
        gasto <- consumo * costosGalon[i]
        Escribir "El gasto para viajar a ", destinos[i], " es: S/.", gasto
    FinPara
FinAlgoritmo