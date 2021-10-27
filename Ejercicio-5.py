# Pseudocódigo
# 1. Variables: cantidadGasolina, precioGasolinaPorLitro=4.5
# 2. Inicio
# 3. Escribir("Ingrese lo que "surten" en galones,es decir, la cantidad de gasolina :")
# 4. Leer (cantidadGasolina)
# 5. pagoCliente = cantidadGasolina* precioGasolinaPorLitro
# 6. Escribir("El dinero que paga el cliente es": " + str(pagoCliente))
# 7. Fin


print("Lo que surgen en galones")
cantidadGasolina= float(input())

precioGasolinaPorLitro= 4.5

pagoCliente= cantidadGasolina* precioGasolinaPorLitro

print("El dinero que paga el cliente es:" +str(pagoCliente))