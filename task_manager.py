import os

# Lista global para almacenar las tareas
tasks = []

def clear_console():
    """Limpia la consola para una mejor experiencia del usuario."""
    os.system("cls" if os.name == "nt" else "clear")

def display_tasks():
    """Muestra todas las tareas."""
    if not tasks:
        print("📋 No tienes tareas en tu lista.")
    else:
        print("\n📋 Lista de Tareas:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{index}. {task['name']} {status}")

def add_task():
    """Agrega una nueva tarea."""
    task_name = input("➕ Ingresa el nombre de la tarea: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"✅ Tarea '{task_name}' añadida con éxito.")
    else:
        print("⚠️ El nombre de la tarea no puede estar vacío.")

def complete_task():
    """Marca una tarea como completada."""
    display_tasks()
    try:
        task_number = int(input("\n🔢 Ingresa el número de la tarea a completar: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("✅ Tarea marcada como completada.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Debes ingresar un número.")

def delete_task():
    """Elimina una tarea."""
    display_tasks()
    try:
        task_number = int(input("\n🗑️ Ingresa el número de la tarea a eliminar: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"🗑️ Tarea '{removed_task['name']}' eliminada con éxito.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Debes ingresar un número.")

def main_menu():
    """Muestra el menú principal."""
    while True:
        clear_console()
        print("📝 Administrador de Tareas")
        print("1. Ver Tareas")
        print("2. Agregar Tarea")
        print("3. Completar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")

        choice = input("\nSelecciona una opción (1-5): ").strip()

        if choice == "1":
            clear_console()
            display_tasks()
            input("\nPresiona Enter para continuar...")
        elif choice == "2":
            add_task()
            input("\nPresiona Enter para continuar...")
        elif choice == "3":
            complete_task()
            input("\nPresiona Enter para continuar...")
        elif choice == "4":
            delete_task()
            input("\nPresiona Enter para continuar...")
        elif choice == "5":
            print("👋 ¡Gracias por usar el Administrador de Tareas!")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main_menu()
