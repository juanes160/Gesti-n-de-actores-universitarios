# curso.py (Clase Curso)

class Curso:
    def _init_(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes_matriculados = []
    
    def matricular_estudiante(self, estudiante):
        self.estudiantes_matriculados.append(estudiante)
        print(f"{estudiante.get_nombre()} ha sido matriculado en {self.nombre}.")
    
    def mostrar_estudiantes(self):
        if not self.estudiantes_matriculados:
            print(f"No hay estudiantes matriculados en {self.nombre}.")
        else:
            print(f"Estudiantes en {self.nombre}:")
            for estudiante in self.estudiantes_matriculados:
                print(estudiante)
    
    def _str_(self):
        return f"Curso: {self.nombre} (Código: {self.codigo})"