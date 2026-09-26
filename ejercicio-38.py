"""
37. Escribe un programa que determine qué calificación en texto
tiene un alumno según su calificación numérica.

0 - 69: insuficiente
70 - 79: bien
80 - 89: muy bien
90 - 100: excelente
"""

calificacion = int(input("Introduce la calificación: "))

if calificacion >= 0 and calificacion <= 69:
    print("Insuficiente")
elif calificacion <= 79:
    print("Bien")
elif calificacion <= 89:
    print("Muy bien")
elif calificacion <= 100:
    print("Excelente")
else:
    print("Calificación no válida.")