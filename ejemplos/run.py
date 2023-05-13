"""

"""
# Crear dos objetos de la clase 01
# Presentar objeto; usar el método __st__

# Presentar objeto; usar el método __st__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años."
        

# Objeto 1
persona1 = Persona("Gabriel", 18)

# Presentar objeto 1
print(persona1)

# Objeto 2
# crear ingresando valores por teclado
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
persona2 = Persona(nombre, edad)

# Presentar objeto 2
print(persona2)
