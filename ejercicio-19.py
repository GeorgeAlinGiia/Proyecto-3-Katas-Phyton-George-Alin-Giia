"""
1. Crea una función lambda que filtre los números impares de una lista dada.
"""

filtrarImpares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filtrarImpares(listaNumeros))