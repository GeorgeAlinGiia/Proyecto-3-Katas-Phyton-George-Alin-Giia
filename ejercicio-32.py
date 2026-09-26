"""
1. Crea una función que tome un nombre completo y una lista de empleados,
busque el nombre en la lista y devuelva el puesto del empleado si se encuentra;
de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""

def buscarEmpleado(nombreInput: str, empleados: list) -> str:
    for empleado in empleados:
        if empleado["nombre"] == nombreInput:
            return empleado["puesto"]
    
    return "La persona no trabaja aquí."


empleados = [
    {"nombre": "Dani García", "puesto": "Programador"},
    {"nombre": "Laura López", "puesto": "Diseñadora"},
    {"nombre": "Carlos Pérez", "puesto": "Administrador"}
]

nombre = input("Introduce el nombre completo: ")

print(buscarEmpleado(nombre, empleados))