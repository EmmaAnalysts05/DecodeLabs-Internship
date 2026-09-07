# todo.py

import json

my_tasks = []  # This will hold dictionaries like {"id": 1, "task": "Buy Milk"}

def save_tasks():
    with open("Task.json", "w") as file:
        json.dump(my_tasks, file, indent=4)
    print("Tasks saved to Task.json")

def load_tasks():
    global my_tasks
    try:
        with open("Task.json", "r") as file:
            my_tasks = json.load(file)
        print("Tasks loaded from Task.json")
    except FileNotFoundError:
        my_tasks = []
        print("No saved tasks found, starting fresh.")

def add_task(task):
    # Each task is a dictionary with an ID and description
    new_task = {"id": len(my_tasks) + 1, "task": task}
    my_tasks.append(new_task)
    save_tasks()
    print(f"Task added: {new_task['task']}")

def view_tasks():
    if not my_tasks:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for task in my_tasks:
            print(f"{task['id']}. {task['task']}")

def main():
    load_tasks()  # Load saved tasks at startup
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            task = input("Enter your task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()