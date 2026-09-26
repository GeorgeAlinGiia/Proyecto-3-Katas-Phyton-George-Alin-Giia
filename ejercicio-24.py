"""
1. Calcula la diferencia total en los valores de una lista.
Usa la función reduce().
"""

from functools import reduce

def diferenciaTotal(numeros: list) -> int:
    return reduce(lambda total, numero: total - numero, numeros)


listaNumeros = [20, 5, 3, 2]

print(diferenciaTotal(listaNumeros))