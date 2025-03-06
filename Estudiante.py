class Estudiante:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Estudiante: {self.nombre}, Cédula: {self.cedula}"
