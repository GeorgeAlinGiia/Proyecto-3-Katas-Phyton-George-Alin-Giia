"""
39. Programa para calcular el precio final de una compra
aplicando un cupón de descuento.
"""

precio = float(input("Introduce el precio original: "))

tieneCupon = input("¿Tienes un cupón de descuento? (sí/no): ")

if tieneCupon == "sí":
    descuento = float(input("Introduce el valor del descuento (%): "))

    if descuento > 0:
        precioFinal = precio - (precio * descuento / 100)
        print("El precio final es:", precioFinal)
    else:
        print("El cupón no es válido.")
        print("El precio final es:", precio)

elif tieneCupon == "no":
    print("El precio final es:", precio)

else:
    print("Respuesta no válida.")