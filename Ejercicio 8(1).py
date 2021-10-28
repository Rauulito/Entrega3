import random


#Generamos número aleatorio entre el 1 y el 15
numeroAleatorio = random.randint(1, 15)

numeroUsuario = 0
numeroUsuario = int(numeroUsuario)

while numeroUsuario != numeroAleatorio :
    num_usuario = int(input("Ingresa un número entre el 1 y el 300: "))
    if numeroAleatorio > numeroUsuario:
        print("Escribe un número mayor")
    elif numeroAleatorio < numeroUsuario:
        print("Escribe un número menor")


if numeroUsuario == numeroAleatorio:
    print("El número acertado es " + str(numeroAleatorio))


