# menu_profesor.py (Menú de Profesores)

from Profesor import Profesor

list_profesores = []

def agregar_profesor():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    direccion = input("Ingrese la dirección: ")
    materia = input("Ingrese la materia que enseña: ")
    
    profesor = Profesor(nombre, edad, direccion, materia)
    list_profesores.append(profesor)
    print("Profesor agregado correctamente.")

def mostrar_profesores():
    if not list_profesores:
        print("No hay profesores registrados.")
    else:
        for profesor in list_profesores:
            print(profesor)

def menu_profesor():
    while True:
        print("\n::: MENÚ PROFESORES :::")
        print("1. Agregar Profesor")
        print("2. Mostrar Profesores")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_profesor()
        elif opcion == "2":
            mostrar_profesores()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_profesor()