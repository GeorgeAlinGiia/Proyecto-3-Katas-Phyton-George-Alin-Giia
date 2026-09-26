"""
7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

def convertirDatos(datos):
    return list(map(lambda elemento: str(elemento), datos))


alumnos = [("George", 6.9, "Aprobado"), ("Laura", 6, "Aprobado")]

resultado = convertirDatos(alumnos)

print(resultado)