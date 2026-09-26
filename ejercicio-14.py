"""
1. Crea una función que retorne las palabras de una lista que comiencen
con una letra en específico. Usa la función filter().
"""

def filtrarPalabras(palabras: list, letra: str) -> list:
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


listaPalabras = ["casa", "coche", "perro", "camino", "gato"]

print(filtrarPalabras(listaPalabras, "c"))