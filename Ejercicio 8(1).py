import random

#Numero aleatorio del 1 al 15
numeroAleatorio= random.randint(1,15)

while (numeroUsuario != numeroAleatorio):
    numeroUsuario= int(input("Ingresa un numero entre 1 y 300:"))
    if numeroAleatorio < numeroUsuario:
        print("Escribe un numero más pequeño")
    if numeroAleatorio > numeroUsuario:
        print("Escribe un numero más grande")
    else:
        break
  

if numeroUsuario == numeroAleatorio
   print("El número acertado es:" + str(numeroAleatorio) + "en" + str(contadorIntentos))
