"""
1. Crea la clase Arbol

- Define un árbol genérico con un tronco y ramas como atributos.
- Métodos: crecer_tronco, nueva_rama, crecer_ramas,
  quitar_rama, info_arbol.
"""


class Arbol:

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for posicion in range(len(self.ramas)):
            self.ramas[posicion] += 1

    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitud de las ramas": self.ramas
        }


# Caso de uso

arbol = Arbol()

# b. Hacer crecer el tronco una unidad
arbol.crecer_tronco()

# c. Añadir una nueva rama
arbol.nueva_rama()

# d. Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# e. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# f. Retirar la rama situada en la posición 2
arbol.quitar_rama(1)

# g. Obtener información sobre el árbol
print(arbol.info_arbol())