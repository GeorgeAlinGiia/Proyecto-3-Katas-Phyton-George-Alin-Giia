"""
1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
"""
def freqLetter(dataInput: str) -> dict:
    dataInput = dataInput.replace(" ","").lower() 
    
    newDict = {}
    for index in dataInput:
          newDict[index] = dataInput.count(index)
    return newDict 

diccionario = freqLetter(textoEntregar)
print(diccionario)