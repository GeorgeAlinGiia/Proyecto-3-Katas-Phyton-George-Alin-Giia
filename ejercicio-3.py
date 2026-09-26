"""
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""

listaPalabras = ['manzana', 'platano', 'mandarinas','pera', 'mango']
palabraObjetivo = 'ra'

def busqPalabra(pObj: str, lista: list) -> list:
    
    listaPalabrasIguales = []
    for index in lista:
        if index.__contains__(pObj):
            listaPalabrasIguales.append(index)
    return listaPalabrasIguales

listaObjetivo = busqPalabra(palabraObjetivo, listaPalabras)
print(listaObjetivo)