# Lista de tareas
tareas = ["Tarea A", "Tarea B", "Tarea C"]

# Función para agregar una tarea a la lista
def agregar_tarea(lista):
    # Entrada para la tarea
    tarea = input("Introduzca la descripción de la tarea: ")

    # Añadir la tarea al final de la lista
    lista.append(tarea)

    # Informe de tarea añadida
    print("\nLa tarea se añadió a la lista de tareas pendientes.\n")

    # Imprime la tarea añadida
    print(f"La tarea añadida es: {tarea}.")

    # Informa del número de tarea
    print(f"La tarea se almacenó en la posición {len(lista)}\n")

# Función para ver todas las tareas en la lista
def ver_tareas(lista):
    # Condicional que evalúa si algo está en la lista
    if lista:
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}")
    else:
        print("No hay tareas pendientes.")
    print("--- FIN DEL LISTADO DE TAREAS ---")

# Función para marcar una tarea como completada
def tarea_completada(lista):
    ver_tareas(lista)
    try:
        # Entrada para que el usuario introduzca una tarea
        completada = int(input("Introduzca el número de la tarea a marcar como completada: "))

        if completada > 0 and completada <= len(lista):
            if "(Completada)" in lista[completada - 1]:
                print("La tarea ya estaba marcada como completada.")
            else:
                lista[completada - 1] = "(Completada) " + lista[completada - 1]
                print("Se marcó la tarea como completada.")
        else:
            print("Opción inválida. El número ingresado no corresponde a ninguna tarea.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Función para eliminar una tarea de la lista
def eliminar_tarea(lista):
    if lista:
        ver_tareas(lista)
        try:
            # Entrada para que el usuario introduzca una tarea
            tarea = int(input("Introduzca el número de la tarea a eliminar: "))

            if tarea > 0 and tarea <= len(lista):
                del lista[tarea - 1]
                print("Se eliminó la tarea.")
            else:
                print("Opción inválida. El número ingresado no corresponde a ninguna tarea.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    else:
        print("No hay tareas.")
