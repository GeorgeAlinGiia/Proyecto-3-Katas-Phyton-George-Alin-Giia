"""
1. Dada una lista numérica, obtén el producto total de los valores.
Usa la función reduce().
"""

from functools import reduce

def productoTotal(numeros: list) -> int:
    return reduce(lambda total, numero: total * numero, numeros)


listaNumeros = [2, 3, 4, 5]

print(productoTotal(listaNumeros))