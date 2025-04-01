estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    materias = input("Materias aprobadas (separadas por coma): ").split(', ')
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print(f"Estudiante {nombre} agregado correctamente.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    for nombre, info in estudiantes.items():
        print(f"Nombre: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}")
    print()

def eliminar_estudiante():
    nombre = input("Nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado correctamente.\n")
    else:
        print("El estudiante no existe.\n")

def buscar_estudiante():
    nombre = input("Nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        info = estudiantes[nombre]
        print(f"Nombre: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}\n")
    else:
        print("El estudiante no existe.\n")

def verificar_palabra_clave():
    palabra = input("Ingrese la palabra clave a buscar en los nombres: ")
    coincidencias = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower()]
    if coincidencias:
        print("Estudiantes encontrados:")
        for nombre in coincidencias:
            print(f"- {nombre}")
    else:
        print("No se encontraron coincidencias.\n")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante")
        print("5. Verificar palabra clave en nombres")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                verificar_palabra_clave()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, intente nuevamente.\n")

menu()