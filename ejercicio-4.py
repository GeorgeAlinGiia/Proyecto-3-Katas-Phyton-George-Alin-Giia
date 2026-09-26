"""
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
"""
listaA = [55, 63, 44, 552, 99, 41]
listaB = [10, 20, 30, 40, 50, 60]

def difListas(listaPrimera: list, listaSegunda: list) -> list:
    return list(map(lambda a, b: a - b , listaPrimera, listaSegunda))

diferValue = difListas(listaA, listaB)
print (diferValue)