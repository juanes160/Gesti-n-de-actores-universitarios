# Menu.py (Menú Principal)

import menu_estudiante
import menu_profesor

def menu_principal():
    while True:
        print("\n::: MENÚ PRINCIPAL :::")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Profesores")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_estudiante.menu_estudiante()
        elif opcion == "2":
            menu_profesor.menu_profesor()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()