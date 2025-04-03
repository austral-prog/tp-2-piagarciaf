def change():
	pesos= 100
	gasto= 23.75
	vuelto= pesos - gasto #con centavos inluidos
	vueltosin= int(pesos - gasto) #num redondo
	centavos= int((vuelto - vueltosin)* 100) 
	print ("Ingresar gasto:")
	print(gasto)

	print ("Dinero recibido")
	print(pesos)
	print ("\nVuelto\n")
	print("Pesos:")
	print(vueltosin)
	print("Centavos:")
	print(centavos)
