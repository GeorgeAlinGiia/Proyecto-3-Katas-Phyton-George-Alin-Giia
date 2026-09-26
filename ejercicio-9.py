"""
1. Escribe una función que tome una lista de nombres de mascotas como parámetro
y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
Usa la función filter().
"""

def filtrarMascotas(mascotas):
    mascotasProhibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    return list(filter(lambda mascota: mascota not in mascotasProhibidas, mascotas))


misMascotas = ["Perro", "Tigre", "Gato", "Oso", "Conejo"]

print(filtrarMascotas(misMascotas))