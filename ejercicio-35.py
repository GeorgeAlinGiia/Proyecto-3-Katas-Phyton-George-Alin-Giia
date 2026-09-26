"""
35. Crea la clase UsuarioBanco

- Representa a un usuario de un banco con su nombre, saldo
  y si tiene o no cuenta corriente.
- Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
"""


class UsuarioBanco:

    def __init__(self, nombre, saldo, cuentaCorriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuentaCorriente = cuentaCorriente

    def retirar_dinero(self, cantidad):
        if not self.cuentaCorriente:
            raise ValueError("El usuario no tiene cuenta corriente.")

        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo.")

        self.saldo -= cantidad

    def transferir_dinero(self, otroUsuario, cantidad):
        if not self.cuentaCorriente:
            raise ValueError("El usuario no tiene cuenta corriente.")

        self.retirar_dinero(cantidad)
        otroUsuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad


# Caso de uso

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# b. Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)

# c. Transferir 80 unidades de Bob a Alicia
bob.transferir_dinero(alicia, 80)

# d. Retirar 50 unidades del saldo de Alicia
alicia.retirar_dinero(50)

print("Saldo de Alicia:", alicia.saldo)
print("Saldo de Bob:", bob.saldo)