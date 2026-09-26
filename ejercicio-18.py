"""
1. Escribe un programa en Python que cree una lista de diccionarios
con información de estudiantes (nombre, edad, calificación) y use
filter para extraer a los estudiantes con una calificación mayor o igual a 90.
"""

estudiantes = [
    {"nombre": "Dani", "edad": 20, "calificacion": 95},
    {"nombre": "Laura", "edad": 21, "calificacion": 85},
    {"nombre": "Carlos", "edad": 19, "calificacion": 92},
    {"nombre": "Marta", "edad": 22, "calificacion": 78}
]

estudiantesAprobados = list(
    filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)
)

print(estudiantesAprobados)