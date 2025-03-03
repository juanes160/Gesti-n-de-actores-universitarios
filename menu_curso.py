# menu_curso.py (Menú de Cursos)

from Curso import Curso
from Estudiante import Estudiante

list_cursos = []

def agregar_curso():
    nombre = input("Ingrese el nombre del curso: ")
    codigo = input("Ingrese el código del curso: ")
    curso = Curso(nombre, codigo)
    list_cursos.append(curso)
    print("Curso agregado correctamente.")

def mostrar_cursos():
    if not list_cursos:
        print("No hay cursos registrados.")
    else:
        for curso in list_cursos:
            print(curso)

def matricular_estudiante():
    if not list_cursos:
        print("No hay cursos disponibles para matricular estudiantes.")
        return
    
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    direccion = input("Ingrese la dirección del estudiante: ")
    curso_codigo = input("Ingrese el código del curso en el que desea matricularse: ")
    
    estudiante = Estudiante(nombre, edad, direccion, curso_codigo)
    for curso in list_cursos:
        if curso.codigo == curso_codigo:
            curso.matricular_estudiante(estudiante)
            return
    
    print("Curso no encontrado.")

def menu_curso():
    while True:
        print("\n::: MENÚ CURSOS :::")
        print("1. Agregar Curso")
        print("2. Mostrar Cursos")
        print("3. Matricular Estudiante")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_curso()
        elif opcion == "2":
            mostrar_cursos()
        elif opcion == "3":
            matricular_estudiante()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if _name_ == "_main_":
    menu_curso()