from Curso import Curso
from menu_profesor import lista_profesores
from menu_estudiante import lista_estudiantes

lista_cursos = []

def agregar_curso():
    nombre = input("Ingrese el nombre del curso: ")
    codigo = input("Ingrese el código del curso: ")
    profesor_nombre = input("Ingrese el nombre del profesor a cargo: ").strip().lower()

    profesor_encontrado = next((prof for prof in lista_profesores if prof.nombre.strip().lower() == profesor_nombre), None)

    if not profesor_encontrado:
        print("Profesor no encontrado. Debe registrar primero al profesor.")
        return

    curso = Curso(nombre, codigo, profesor_encontrado)
    lista_cursos.append(curso)
    print(f"Curso {nombre} registrado con éxito.")

def listar_cursos():
    if not lista_cursos:
        print("No hay cursos registrados.")
    else:
        for curso in lista_cursos:
            print(curso)

def inscribir_estudiante():
    if not lista_cursos:
        print("No hay cursos disponibles.")
        return

    cedula = input("Ingrese la cédula del estudiante: ")
    estudiante = next((est for est in lista_estudiantes if est.cedula == cedula), None)

    if not estudiante:
        print("Estudiante no encontrado. Debe registrarlo primero.")
        return

    print("Cursos disponibles:")
    for i, curso in enumerate(lista_cursos, start=1):
        print(f"{i}. {curso.nombre} (Código: {curso.codigo})")

    opcion = int(input("Seleccione el número del curso: ")) - 1

    if 0 <= opcion < len(lista_cursos):
        curso_seleccionado = lista_cursos[opcion]
        curso_seleccionado.inscribir_estudiante(estudiante)
        print(f"Estudiante {estudiante.nombre} inscrito en {curso_seleccionado.nombre}.")
    else:
        print("Opción inválida.")

def listar_cursos_con_estudiantes():
    if not lista_cursos:
        print("No hay cursos registrados.")
        return

    for curso in lista_cursos:
        print(f"\nCurso: {curso.nombre} (Código: {curso.codigo})")
        print("Profesor:", curso.profesor.nombre)
        print("Estudiantes inscritos:")
        print(curso.listar_estudiantes())

def menu_curso():
    while True:
        print("\n--- Menú Curso ---")
        print("1. Agregar curso")
        print("2. Listar cursos")
        print("3. Inscribir estudiante en un curso")
        print("4. Ver cursos con estudiantes inscritos")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_curso()
        elif opcion == "2":
            listar_cursos()
        elif opcion == "3":
            inscribir_estudiante()
        elif opcion == "4":
            listar_cursos_con_estudiantes()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
