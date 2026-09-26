"""
1. Escribe una función que tome una cadena de texto y un número entero n
como parámetros y devuelva una lista de todas las palabras que sean más
largas que n. Usa la función filter().
"""

def palabrasLargas(texto: str, n: int) -> list:
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


textoInput = "Hola me llamo Dani y estoy aprendiendo Python"

print(palabrasLargas(textoInput, 4))