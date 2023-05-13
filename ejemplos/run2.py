"""

"""
# Crear dos objetos de la clase 02


# Presentar objeto; usar el método __st__


# Presentar objeto; usar el método __st__


class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        
    def __str__(self):
        return f"Mi nombre es {self.nombre} y soy un perro de raza {self.raza}."
        

# Objeto 1
perro1 = Perro("Lucas", "Golden")

# Presentar objeto 1
print(perro1)


# Objeto 2
# crear ingresando valores por teclado
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
perro2 = Perro(nombre, raza)

# Presentar objeto 2
print(perro2)
