import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for idx, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{idx+1}. [{status}] {task['task']}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)


def delete_task(tasks):
    display_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
