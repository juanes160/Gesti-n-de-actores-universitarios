# menu_estudiante.py (Menú de Estudiantes)

from Estudiante import Estudiante

list_estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    direccion = input("Ingrese la dirección: ")
    curso = input("Ingrese el curso: ")
    
    estudiante = Estudiante(nombre, edad, direccion, curso)
    list_estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")

def mostrar_estudiantes():
    if not list_estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in list_estudiantes:
            print(estudiante)

def menu_estudiante():
    while True:
        print("\n::: MENÚ ESTUDIANTES :::")
        print("1. Agregar Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_estudiante()