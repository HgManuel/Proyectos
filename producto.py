producto= (input("Ingrese el nombre del producto: "))
costoP= float(input("El costo de produccion es: "))
utilidad= costoP*1.2
impuestos= costoP*0.15
precioV= float(costoP) + float(utilidad) + float(impuestos)
print("El precio de venta del articulo es de: ", precioV)
