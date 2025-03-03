# Persona.py (Clase Base)

class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}"
