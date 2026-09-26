"""
1. Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

def contarCaracteres(texto: str) -> int:
    return len(texto)


textoInput = "Hola mundo"

print(contarCaracteres(textoInput))