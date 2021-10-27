print("Número de respuestas correctas")
respuestasCorrectas= float(input())

print("Número de respuestas incorrectas")
respuestasIncorrectas= float(input())

print("Número de respuestas en blanco")
respuestasEnBlanco= float(input())

puntajeFinal= respuestasCorrectas*3 + respuestasIncorrectas*-1 + respuestasEnBlanco*0  
print("La puntuación final es:" +str(puntajeFinal))