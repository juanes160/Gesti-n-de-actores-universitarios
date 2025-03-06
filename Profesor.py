class Profesor:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Profesor: {self.nombre}, Cédula: {self.cedula}"
