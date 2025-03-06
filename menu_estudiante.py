from Estudiante import Estudiante

lista_estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    cedula = input("Ingrese la cédula del estudiante: ")

    estudiante = Estudiante(nombre, cedula)
    lista_estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado con éxito.")

def listar_estudiantes():
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in lista_estudiantes:
            print(estudiante)

def eliminar_estudiante():
    cedula = input("Ingrese la cédula del estudiante a eliminar: ")
    
    for estudiante in lista_estudiantes:
        if estudiante.cedula == cedula:
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante.nombre} eliminado con éxito.")
            return
    
    print("Estudiante no encontrado.")

def menu_estudiante():
    while True:
        print("\n--- Menú Estudiante ---")
        print("1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            eliminar_estudiante()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
