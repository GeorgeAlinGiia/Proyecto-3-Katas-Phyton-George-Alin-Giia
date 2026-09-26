"""
1. Genera una función que, para un conjunto de caracteres, devuelva una lista
de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar
repetidas. Usa la función map().
"""

def mayusMinus(caracteres: set) -> list:
    caracteres = set(caracteres)
    return list(map(lambda letra: (letra.upper(), letra.lower()), caracteres))


letras = {"a", "b", "c", "a", "B"}

print(mayusMinus(letras))