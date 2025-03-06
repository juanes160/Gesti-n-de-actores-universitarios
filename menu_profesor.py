from Profesor import Profesor

lista_profesores = []

def agregar_profesor():
    nombre = input("Ingrese el nombre del profesor: ")
    cedula = input("Ingrese la cédula del profesor: ")

    profesor = Profesor(nombre, cedula)
    lista_profesores.append(profesor)
    print(f"Profesor {nombre} agregado con éxito.")

def listar_profesores():
    if not lista_profesores:
        print("No hay profesores registrados.")
    else:
        for profesor in lista_profesores:
            print(profesor)

def eliminar_profesor():
    cedula = input("Ingrese la cédula del profesor a eliminar: ")
    
    for profesor in lista_profesores:
        if profesor.cedula == cedula:
            lista_profesores.remove(profesor)
            print(f"Profesor {profesor.nombre} eliminado con éxito.")
            return
    
    print("Profesor no encontrado.")

def menu_profesor():
    while True:
        print("\n--- Menú Profesor ---")
        print("1. Agregar profesor")
        print("2. Listar profesores")
        print("3. Eliminar profesor")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_profesor()
        elif opcion == "2":
            listar_profesores()
        elif opcion == "3":
            eliminar_profesor()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
