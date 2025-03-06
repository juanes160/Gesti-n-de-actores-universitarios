class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []  # Lista de estudiantes inscritos

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        if not self.estudiantes:
            return "No hay estudiantes inscritos en este curso."
        return "\n".join([str(estudiante) for estudiante in self.estudiantes])

    def __str__(self):
        return f"Curso: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor.nombre}"
