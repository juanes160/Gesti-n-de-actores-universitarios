from menu_profesor import menu_profesor
from menu_curso import menu_curso
from menu_estudiante import menu_estudiante

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Profesores")
        print("2. Gestión de Cursos")
        print("3. Gestión de Estudiantes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_profesor()
        elif opcion == "2":
            menu_curso()
        elif opcion == "3":
            menu_estudiante()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()