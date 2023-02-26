import json

def add_task(task_list):
    """Add a new task to the task list."""
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task = {"name": task_name, "description": task_description}
    task_list.append(task)
    print("Task added successfully.")

def delete_task(task_list):
    """Delete a task from the task list."""
    task_index = int(input("Enter the task index to delete: "))
    del task_list[task_index]
    print("Task deleted successfully.")

def show_tasks(task_list):
    """Display all tasks in the task list."""
    for index, task in enumerate(task_list):
        print(f"{index}. {task['name']}: {task['description']}")

def save_tasks(task_list):
    """Save the task list to a JSON file."""
    with open("tasks.json", "w") as f:
        json.dump(task_list, f)
    print("Tasks saved successfully.")

def load_tasks():
    """Load the task list from a JSON file."""
    try:
        with open("tasks.json", "r") as f:
            task_list = json.load(f)
    except FileNotFoundError:
        task_list = []
    return task_list

def main():
    """Main function to run the To-Do List application."""
    task_list = load_tasks()

    while True:
        print("\nTo-Do List\n----------")
        show_tasks(task_list)
        print("\nMenu\n----")
        print("1. Add task")
        print("2. Delete task")
        print("3. Save tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            delete_task(task_list)
        elif choice == "3":
            save_tasks(task_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
