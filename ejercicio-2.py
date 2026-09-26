"""
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""
lista = [33,7,9,55,77,66,10,333]
newLista = list(map(lambda numero: numero * 2, lista))

print(lista)
print(newLista)