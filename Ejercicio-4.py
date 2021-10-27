print("Número de partidos ganados")
partidosGanados= float(input())

print("Número de partidos empatados")
partidosEmpatados= float(input())

print("Número de partidos perdidos")
partidosPerdidos= float(input())

puntajeFinal= partidosGanados*3 + partidosEmpatados*1 + partidosPerdidos*0

print("La puntuación final es:" +str(puntajeFinal))