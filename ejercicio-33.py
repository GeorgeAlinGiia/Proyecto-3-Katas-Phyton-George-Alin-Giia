"""
1. Crea una función lambda que sume elementos correspondientes
de dos listas dadas.
"""

sumarListas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

print(sumarListas(lista1, lista2))