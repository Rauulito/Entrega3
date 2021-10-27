# Pseudocódigo
# 1. Variables: N1(nota primer parcial), N2(nota segundo parcial), N1(nota tercer parcial)
# 2. Inicio
# 3. Escribir("Ingrese la nota del primer parcial:")
# 4. Leer (N1)
# 5. Escribir("Ingrese la nota del segundo parcial:")
# 6. Leer (N2)
# 7. Escribir("Ingrese la nota del tercer parcial:")
# 8. Leer (N3)
# 9. promedioSimple = (N1 * N2 *N3)/ 3
# 10. Escribir("La media de las notas parciales es : " + str(promedioSimple))
# 11. Fin

print("Ingrese la nota del primer parcial:")
N1 = float(input())

print("Ingrese la nota del segundo parcial:")
N2 = float(input())

print("Ingrese la nota del tercer parcial:")
N3 = float(input())

promedioSimple = (N1 + N2 + N3) / 3

print("La media de las notas parciales es: " + str(promedioSimple))

