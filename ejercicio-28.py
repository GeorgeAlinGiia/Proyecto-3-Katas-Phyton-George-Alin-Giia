"""
1. Crea una función que busque y devuelva el primer elemento duplicado
en una lista dada.
"""

def primerDuplicado(lista: list):
    elementosVistos = set()

    for elemento in lista:
        if elemento in elementosVistos:
            return elemento

        elementosVistos.add(elemento)

    return None


listaDatos = [5, 2, 8, 3, 2, 7, 5]

print(primerDuplicado(listaDatos))