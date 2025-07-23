# TO-DO-LIST:(project.py)

list = []
def add_task(task):
    """Add a new task to the list."""
    list.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    """Remove a task from the list."""
    if task in list:
        list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    """View all tasks in the list."""
    if list:
        print("Current tasks:")
        for task in list:
            print(f"- {task}")
    else:
        print("No tasks in the list.")

def completed_task(task):
    """ displays completed task"""
    if task in list:
        list.remove(task)
    print(f"Task '{task}' marked as completed.")
    print("Completed tasks are not stored in the list.")


print("Welcome to the To-Do List App!")
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Mark task as completed")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        task = input("Enter the task to mark as completed: ")
        completed_task(task)
    elif choice == '5':
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid option, please try again.")
        