"""
1. Crea una función que solicite al usuario ingresar una lista de nombres
y luego un nombre para buscar en esa lista. Si el nombre está en la lista,
imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
"""

class NombreNoEncontradoError(Exception):
    pass


def buscarNombre():
    nombres = input("Introduce los nombres separados por comas: ").split(",")
    nombreBuscar = input("Introduce el nombre que quieres buscar: ")

    nombres = [nombre.strip() for nombre in nombres]

    if nombreBuscar in nombres:
        print("El nombre ha sido encontrado.")
    else:
        raise NombreNoEncontradoError("El nombre no está en la lista.")


try:
    buscarNombre()
except NombreNoEncontradoError as error:
    print("Error:", error)