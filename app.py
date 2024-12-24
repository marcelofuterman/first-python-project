# Simple programa para gestionar tareas pendientes
tasks = []

def show_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

while True:
    show_menu()
    choice = input("Selecciona una opción: ")

    if choice == "1":
        task = input("Ingresa la tarea: ")
        tasks.append(task)
        print(f"Tarea '{task}' añadida.")
    elif choice == "2":
        if tasks:
            print("\n--- Tareas pendientes ---")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No hay tareas pendientes.")
    elif choice == "3":
        if tasks:
            print("\n--- Eliminar tarea ---")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            try:
                task_to_remove = int(input("Ingresa el número de la tarea a eliminar: "))
                removed_task = tasks.pop(task_to_remove - 1)
                print(f"Tarea '{removed_task}' eliminada.")
            except (ValueError, IndexError):
                print("Opción inválida.")
        else:
            print("No hay tareas para eliminar.")
    elif choice == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
