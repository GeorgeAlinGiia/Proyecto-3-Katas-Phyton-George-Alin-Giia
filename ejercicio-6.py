"""
6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def calcFactorialRecursivo(numInput: int) -> int:
    if numInput == 0:
        return 1
    return numInput * calcFactorialRecursivo(numInput - 1)


numFactorial = 5

valueData = calcFactorialRecursivo(numFactorial)
print(valueData)