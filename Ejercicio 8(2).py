import random

# Creamos e incializamos contador de intentos
contadorIntentos = 0

#Generamos número aleatorio entre el 1 y el 300
numeroAleatorio = random.randint(1,300)
print(numeroAleatorio)
numeroUsuario = 0
numeroUsuario = int(numeroUsuario)

while numeroUsuario != numeroAleatorio and contadorIntentos < 9:
    numeroUsuario = int(input("Ingresa un número entre el 1 y el 300: "))
    if numeroAleatorio > numeroUsuario:
        print("Escribe un número mayor")
    elif numeroAleatorio < numeroUsuario:
        print("Escribe un número menor")
    else:
        break
    contadorIntentos = contadorIntentos + 1

if numeroUsuario == numeroAleatorio:
    print("El número acertado es " + str(numeroAleatorio) + " en " + str(contadorIntentos) + " intentos")
else:
    print("No has acertado el número y se te han acabado los intentos")

