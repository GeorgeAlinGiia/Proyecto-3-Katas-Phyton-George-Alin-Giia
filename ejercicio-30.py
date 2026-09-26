"""
1. Crea una función que determine si dos palabras son anagramas,
es decir, si están formadas por las mismas letras pero en diferente orden.
"""

def sonAnagramas(palabra1: str, palabra2: str) -> bool:
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


palabra1 = "Roma"
palabra2 = "Amor"

print(sonAnagramas(palabra1, palabra2))