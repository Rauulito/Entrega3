import random

#Numero aleatorio del 1 al 300
numeroAleatorio= random.randint(1,300)

contadorIntentos= 0

numeroUsuario= 0
numeroUsuario= int(numeroUsuario)

while (numeroUsuario != numeroAleatorio and contadorIntentos<9):
    numeroUsuario= int(input("Ingresa un numero entre 1 y 300:"))
    if numeroAleatorio < numeroUsuario:
        print("Escribe un numero más pequeño")
    if numeroAleatorio > numeroUsuario:
        print("Escribe un numero más grande")
    else:
        break
    contadorIntentos= contadorIntentos +1

if numeroUsuario ==  numeroAleatorio
    print("El número acertado es:" + str(numeroAleatorio) + "en" + str(contadorIntentos) + "intentos")
else:
    print("No has acertado el número y se te han acabado los intentos")