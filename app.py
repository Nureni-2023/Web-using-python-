# Filename: todo_app.py

import os

# --- Global Data Storage ---
# This list will hold our tasks. Each task will be a dictionary.
# Example task: {"task": "Buy groceries", "completed": False}
tasks = []
FILENAME = "todo_list.txt" # File to save/load tasks

# --- Helper Functions ---

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Python To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")
    print("-------------------------")

def add_task():
    """Prompts the user for a new task and adds it to the list."""
    task_description = input("Enter the task description: ").strip()
    if task_description:
        tasks.append({"task": task_description, "completed": False})
        print(f"Task '{task_description}' added.")
    else:
        print("Task description cannot be empty.")

def view_tasks():
    """Displays all tasks with their completion status."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks in your list. Add some!")
        return

    for i, task_item in enumerate(tasks):
        status = "✓" if task_item["completed"] else " "
        print(f"{i + 1}. [{status}] {task_item['task']}")
    print("------------------")

def mark_task_complete():
    """Marks a task as complete based on its number in the list."""
    view_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            if not tasks[task_num - 1]["completed"]:
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as complete.")
            else:
                print(f"Task '{tasks[task_num - 1]['task']}' is already complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    """Deletes a task based on its number in the list."""
    view_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_tasks():
    """Saves the current tasks to the specified file."""
    try:
        with open(FILENAME, 'w') as f:
            for task_item in tasks:
                # Store as "task_description|completed_status"
                f.write(f"{task_item['task']}|{task_item['completed']}\n")
        print(f"Tasks saved to '{FILENAME}' successfully!")
    except IOError as e:
        print(f"Error saving tasks: {e}")

def load_tasks():
    """Loads tasks from the specified file, replacing current tasks."""
    global tasks # Declare that we are modifying the global 'tasks' list
    if not os.path.exists(FILENAME):
        print(f"No tasks file found at '{FILENAME}'. Starting with an empty list.")
        tasks = [] # Ensure tasks is empty if file doesn't exist
        return

    loaded_tasks = []
    try:
        with open(FILENAME, 'r') as f:
            for line in f:
                line = line.strip()
                if line: # Ensure line is not empty
                    parts = line.split('|', 1) # Split only on the first '|'
                    if len(parts) == 2:
                        task_description = parts[0]
                        completed_status = parts[1].lower() == 'true' # Convert string "True" to boolean True
                        loaded_tasks.append({"task": task_description, "completed": completed_status})
                    else:
                        print(f"Warning: Skipping malformed line in file: {line}")
        tasks = loaded_tasks # Replace current tasks with loaded ones
        print(f"Tasks loaded from '{FILENAME}' successfully!")
    except IOError as e:
        print(f"Error loading tasks: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while loading tasks: {e}")


# --- Main Application Loop ---

def run_app():
    """Runs the main loop of the To-Do List application."""
    load_tasks() # Attempt to load tasks when the app starts
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            load_tasks()
        elif choice == '7':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Entry point of the script
if __name__ == "__main__":
    run_app()
