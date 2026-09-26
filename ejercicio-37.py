"""
37. Genera un programa que nos indique si es de noche,
de día o de tarde según la hora proporcionada por el usuario.
"""

hora = int(input("Introduce la hora (0-23): "))

if hora >= 6 and hora < 12:
    print("Es de día.")
elif hora >= 12 and hora < 20:
    print("Es de tarde.")
elif hora >= 20 or hora < 6:
    print("Es de noche.")
else:
    print("Hora no válida.")