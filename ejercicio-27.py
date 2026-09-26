"""
1. Crea una función que calcule el promedio de una lista de números.
"""

def calcularPromedio(numeros: list) -> float:
    return sum(numeros) / len(numeros)


listaNumeros = [5, 7, 8, 10]

print(calcularPromedio(listaNumeros))