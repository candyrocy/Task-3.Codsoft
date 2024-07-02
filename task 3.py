import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "status": "pending"})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            status = task['status']
            print(f"{i + 1}. {task['task']} - {status}")
    else:
        print("No tasks available.")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task description (or press Enter to keep current): ")
            if new_task:
                tasks[task_num - 1]['task'] = new_task
            new_status = input("Enter the new status (pending/completed): ")
            if new_status in ["pending", "completed"]:
                tasks[task_num - 1]['status'] = new_status
            print(f"Task {task_num} updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()