# Profesor.py (Clase Profesor)

from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, direccion, materia):
        super().__init__(nombre, edad, direccion)
        self.materia = materia
    
    def __str__(self):
        return super().__str__() + f", Materia: {self.materia}"
