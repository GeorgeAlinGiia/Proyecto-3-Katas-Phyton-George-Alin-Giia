"""
1. Para una lista con elementos de tipo integer y string, obtén una nueva
lista solo con los valores int. Usa la función filter().
"""

def filtrarEnteros(lista):
    return list(filter(lambda elemento: isinstance(elemento, int), lista))


listaDatos = [10, "Hola", 25, "Python", 7, "Alin", 30]

print(filtrarEnteros(listaDatos))