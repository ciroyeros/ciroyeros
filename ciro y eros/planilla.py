import sqlite3
conn = sqlite3.connect('Jugadores.db')
cursor = conn.cursor()
def agregar_jugador():
    nombre = input("Nombre del jugador: ")
    edad = int(input("Edad: "))
    documento = input("Documento: ")
    posicion = input("Posición: ")

    try:
        cursor.execute('INSERT INTO planilla (nombre, edad, documento, posicion) VALUES (?, ?, ?, ?)',
                       (nombre, edad, documento, posicion))
        conn.commit()
        print("Jugador agregado.")
    except sqlite3.IntegrityError:
        print("Error: Ya existe un jugador con ese documento.")

def modificar_jugador():
    documento = input("Documento del jugador: ")
    cursor.execute('SELECT * FROM planilla WHERE documento = ?', (documento,))
    jugador = cursor.fetchone()

    if jugador:
        print(f"Jugador encontrado: {jugador}")
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_edad = int(input("Nueva edad: "))
        nueva_posicion = input("Nueva posición: ")
        cursor.execute('''
            UPDATE planilla
            SET nombre = ?, edad = ?, posicion = ?
            WHERE documento = ?
        ''', (nuevo_nombre, nueva_edad, nueva_posicion, documento))
        conn.commit()
        print("Jugador modificado exitosamente.")
    else:
        print("No se encontró el jugador.")

def mostrar_jugadores():
    cursor.execute('SELECT * FROM planilla')
    jugadores = cursor.fetchall()
    if jugadores:
        for jugador in jugadores:
            print(jugador)
    else:
        print("No hay jugadores registrados.")

def eliminar_jugador():
    documento = input("Documento del jugador: ")
    cursor.execute('DELETE FROM planilla WHERE documento = ?', (documento,))
    conn.commit()
    if cursor.rowcount:
        print("Jugador eliminado.")
    else:
        print("No se encontró un jugador con ese documento.")

def buscar_jugador():
    nombre = input("Nombre del jugador: ")
    cursor.execute('SELECT * FROM planilla WHERE nombre LIKE ?', ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    if resultados:
        for jugador in resultados:
            print(jugador)
    else:
        print("No se encontraron jugadores con ese nombre.")


def menu():
    while True:
        print("Menú de Administración de Jugadores")
        print("1. Agregar jugador")
        print("2. Modificar jugador")
        print("3. Mostrar jugadores")
        print("4. Eliminar jugador")
        print("5. Buscar jugador")
        print("6. Salir")

        opcion = input("Elegí una opción: ")

        match opcion:
            case "1":
                agregar_jugador()
            case "2":
                modificar_jugador()
            case "3":
                mostrar_jugadores()
            case "4":
                eliminar_jugador()
            case "5":
                buscar_jugador()
            case "6":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción invalida. Intentá de nuevo.")

menu()



