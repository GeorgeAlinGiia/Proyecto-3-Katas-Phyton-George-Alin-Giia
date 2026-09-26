"""
1. Crea una función que tome una lista de dígitos y devuelva el número
correspondiente. Por ejemplo, [5, 7, 2] corresponde al número 572.
Usa la función reduce().
"""

from functools import reduce


def convertirNumero(digitos: list) -> int:
    return reduce(lambda numero, digito: numero * 10 + digito, digitos)


listaDigitos = [5, 7, 2]

print(convertirNumero(listaDigitos))