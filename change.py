def change():
    pesos= 100
	gasto= 23.75
	vuelto= pesos - gasto #con centavos inluidos 
	vueltosin= int(pesos - gasto) #num redondo
	centavos= int((vuelto - vueltosin)* 100) 
	print (f"Ingresar gasto:\n{gasto}")
	print (f"Dinero recibido\n{pesos}")
	print ("\n\nVuelto")
	print(f"\n\nPesos:\n{vueltosin}")
	print(f"Centavos:\n{centavos}")
change()
