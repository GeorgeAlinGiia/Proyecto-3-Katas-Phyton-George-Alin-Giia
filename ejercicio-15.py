"""
1. Crea una función lambda que sume 3 a cada número de una lista dada.
"""

sumarTres = lambda numeros: [numero + 3 for numero in numeros]

listaNumeros = [1, 2, 3, 4, 5]

print(sumarTres(listaNumeros))