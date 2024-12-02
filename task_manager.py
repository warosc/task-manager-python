import csv
import os

# Nombre del archivo CSV
CSV_FILE = "tasks.csv"

# Función para cargar tareas desde el archivo CSV
def load_tasks():
    tasks = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
    return tasks

# Función para guardar tareas en el archivo CSV
def save_tasks(tasks):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ["id", "task", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

# Función para agregar una nueva tarea
def add_task(task_name):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": str(task_id), "task": task_name, "status": "pendiente"})
    save_tasks(tasks)
    print(f"Tarea '{task_name}' añadida.")

# Función para listar todas las tareas
def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("\nTareas:")
        for task in tasks:
            print(f"[{task['id']}] {task['task']} - {task['status']}")
    else:
        print("No hay tareas registradas.")

# Función para completar una tarea
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == str(task_id):
            task["status"] = "completada"
            save_tasks(tasks)
            print(f"Tarea '{task_id}' marcada como completada.")
            return
    print(f"Tarea con ID '{task_id}' no encontrada.")

# Función para eliminar una tarea
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != str(task_id)]
    save_tasks(tasks)
    print(f"Tarea '{task_id}' eliminada.")

# Menú principal
def main():
    while True:
        print("\n--- Administrador de Tareas ---")
        print("1. Listar tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            task_name = input("Nombre de la tarea: ")
            add_task(task_name)
        elif choice == "3":
            task_id = input("ID de la tarea a completar: ")
            complete_task(task_id)
        elif choice == "4":
            task_id = input("ID de la tarea a eliminar: ")
            delete_task(task_id)
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    main()
