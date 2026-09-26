"""
39. Escribe una función que tome dos parámetros:
figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo")
y datos (una tupla con los datos necesarios para calcular el área).
"""

import math


def calcularArea(figura: str, datos: tuple):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida."


print(calcularArea("rectangulo", (5, 3)))
print(calcularArea("circulo", (4,)))
print(calcularArea("triangulo", (6, 4)))