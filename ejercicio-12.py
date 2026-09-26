"""
1. Genera una función que, al recibir una frase, devuelva una lista
con la longitud de cada palabra. Usa la función map().
"""

def longitudPalabras(frase: str) -> list:
    palabras = frase.split()
    return list(map(len, palabras))


fraseInput = "Hola me llamo Alin"

print(longitudPalabras(fraseInput))