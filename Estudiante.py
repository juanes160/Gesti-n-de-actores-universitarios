# Estudiante.py (Clase Estudiante)

from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)
        self.curso = curso
    
    def __str__(self):
        return super().__str__() + f", Curso: {self.curso}"
