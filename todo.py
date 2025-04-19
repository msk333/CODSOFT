import json
import os

# File to store tasks
TASKS_FILE = "todo_tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.\n")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{idx}. [{status}] {task['description']}")
        print()

# Add a task
def add_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task description cannot be empty!")

# Mark task as complete
def complete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['description']}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

# Update a task
def update_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to update: "))
        if 1 <= index <= len(tasks):
            new_desc = input("Enter new task description: ").strip()
            if new_desc:
                tasks[index - 1]['description'] = new_desc
                save_tasks(tasks)
                print("✏️ Task updated!")
            else:
                print("⚠️ Description cannot be empty!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

# Menu loop
def main():
    tasks = load_tasks()

    while True:
        print("\n🔧 TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task Description")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            update_task(tasks)
        elif choice == '6':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
