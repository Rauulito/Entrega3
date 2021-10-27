# Pseudocódigo
# 1. Variables: respuestasCorrectas, respuestasIncorrectas, respuestasEnBlanco
# 2. Inicio
# 3. Escribir("Ingrese el número de respuestas correctas:")
# 4. Leer (respuestasCorrectas)
# 5. Escribir("Ingrese el número de respuestas incorrectas:")
# 6. Leer (respuestasIncorrectas)
# 7. Escribir("Ingrese el número de respuestas en blanco:")
# 8. Leer (respuestasEnBlanco)
# 9. puntajeFinal = respuestasCorrectas*3 + respuestasIncorrectas*-1 + respuestasEnBlanco*0
# 10. Escribir("La puntuación final es : " + str(puntajeFinal))
# 11. Fin

print("Número de respuestas correctas")
respuestasCorrectas= float(input())

print("Número de respuestas incorrectas")
respuestasIncorrectas= float(input())

print("Número de respuestas en blanco")
respuestasEnBlanco= float(input())

puntajeFinal= respuestasCorrectas*3 + respuestasIncorrectas*-1 + respuestasEnBlanco*0  
print("La puntuación final es:" +str(puntajeFinal))

