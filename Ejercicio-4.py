# Pseudocódigo
# 1. Variables: partidosGanados, partidosEmpatados, partidosPerdidos
# 2. Inicio
# 3. Escribir("Ingrese el número de partidos ganados:")
# 4. Leer (partidosGanados)
# 5. Escribir("Ingrese el número de partidos empatados:")
# 6. Leer (partidosEmpatados)
# 7. Escribir("Ingrese el número de partidos perdidos:")
# 8. Leer (partidosPerdidos)
# 9. puntajeFinal = partidosGanados*3 + partidosEmpatados*1 + partidosPerdidos*0
# 10. Escribir("La puntuación final es : " + str(puntajeFinal))
# 11. Fin

print("Número de partidos ganados")
partidosGanados= float(input())

print("Número de partidos empatados")
partidosEmpatados= float(input())

print("Número de partidos perdidos")
partidosPerdidos= float(input())

puntajeFinal= partidosGanados*3 + partidosEmpatados*1 + partidosPerdidos*0

print("La puntuación final es:" +str(puntajeFinal))