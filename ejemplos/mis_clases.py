"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
persona1 = Persona("Gabriel", 18)
persona1.presentarse()


# clase 02

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"¡Guau! Soy {self.nombre} y soy un perro de raza {self.raza}.")
        
perro1 = Perro("Lucas", "Golden")
perro1.ladrar()
