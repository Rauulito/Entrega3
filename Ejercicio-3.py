print("Número de respuestas correctas")
respuestasCorrectas= float(input())

print("Número de respuestas incorrectas")
respuestasIncorrectas= float(input())

print("Número de respuestas en blanco")
respuestasEnBlanco= float(input())

puntajeFinal= respuestasCorrectas*3 + respuestasIncorrectas*-1  #respuestas en blanco al ser por 0 no va a variar el resultado, por lo tanto no hace falta ponerlas

print("La puntuación final es:" +str(puntajeFinal))