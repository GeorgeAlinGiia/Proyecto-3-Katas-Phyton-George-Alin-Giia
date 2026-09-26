"""
1. Concatena una lista de palabras. Usa la función reduce().
"""

from functools import reduce

def concatenarPalabras(palabras: list) -> str:
    return reduce(lambda palabra1, palabra2: palabra1 + " " + palabra2, palabras)


listaPalabras = ["Hola", "tengo", "tres", "Coches"]

print(concatenarPalabras(listaPalabras))