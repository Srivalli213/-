# Level 2: Intermediate Task 3
# Console application for basic CRUD on tasks

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"[{self.task_id}] {self.title} - {self.description}"


tasks = []
task_counter = 1  # To assign unique IDs


def create_task():
    global task_counter
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append(Task(task_counter, title, description))
    print("✅ Task added successfully!")
    task_counter += 1


def read_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for task in tasks:
            print(task)


def update_task():
    if not tasks:
        print("No tasks to update.")
        return
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            print("✅ Task updated successfully!")
            return
    print("Task not found.")


def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("✅ Task deleted successfully!")
            return
    print("Task not found.")


def menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()
