"""
36. Crea una función llamada procesar_texto

- Procesa un texto según la opción especificada:
  contar_palabras, reemplazar_palabras o eliminar_palabra.
"""


def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}

    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1

    return resultado


def reemplazar_palabras(texto, palabraOriginal, palabraNueva):
    return texto.replace(palabraOriginal, palabraNueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = [elemento for elemento in palabras if elemento != palabra]
    return " ".join(palabras)


def procesar_texto(texto, opcion, *args):

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

    else:
        raise ValueError("Opción no válida.")


# Caso de uso

texto = "Hola mundo Hola Python mundo"

print(procesar_texto(texto, "contar"))

print(procesar_texto(texto, "reemplazar", "Hola", "Adiós"))

print(procesar_texto(texto, "eliminar", "mundo"))