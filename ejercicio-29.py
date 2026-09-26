"""
1. Crea una función que convierta una variable en una cadena de texto
y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""

def enmascararTexto(valor):
    texto = str(valor)
    return "#" * (len(texto) - 4) + texto[-4:]


dato = "1234567890"

print(enmascararTexto(dato))