import funciones 

# Bucle principal
while True:
    # Menú de opciones
    print("\n***** --- Gestor de tareas --- ******\n ")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    # Entrada para el usuario
    opcion = input("Introduzca una opción: ")

    print("\n")

    # Menú de opciones
    match opcion:
        case "1":
            funciones.agregar_tarea(funciones.tareas)

        case "2":
            funciones.ver_tareas(funciones.tareas)

        case "3":
            funciones.tarea_completada(funciones.tareas)

        case "4":
            funciones.eliminar_tarea(funciones.tareas)

        case "5":
            print("Gracias por usar el software. Desconectando...")
            break

        case _:
            print("Opción inválida.")
