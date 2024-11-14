from task import Task, PersonalTask, WorkTask
from task_manager import TaskManager
from datetime import datetime

def create_task(task_manager):
    task_type = input("Enter task type (personal/work): ").strip()
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    if task_type.lower() == "personal":
        description = input("Enter task description: ")
        priority = input("Enter priority (high/medium/low): ")
        task = PersonalTask(description, due_date, priority)

    elif task_type.lower() == "work":
        description = input("Enter task description: ")
        team_members = input("Enter team members (comma-separated): ").split(",")
        task = WorkTask(description, due_date)

        for member in team_members:
            task.add_team_member(member.strip())
    else:
        print("Invalid task type.")
        return None
    return task_manager.add_task(task)
    

def view_tasks(task_manager):
    tasks = task_manager.get_all_tasks()
    if not tasks:
        print("No tasks to display.")
        return

    for task in tasks:
        print(task)

def get_tasks(task_manager):
    task_type = input("Enter task type to filter by (personal/work): ").strip().lower()
    if task_type not in ["personal", "work"]:
        print("Invalid task type.")
        return

    tasks = task_manager.get_tasks(task_type)
    if not tasks:
        print(f"No {task_type} tasks found.")
    else:
        for task in tasks:
            print(task)

def delete_task(task_manager):
    task_id = input("Enter the task ID to delete: ")
    if task_manager.delete_task(task_id):
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"No task found with ID {task_id}.")

def save_tasks_to_csv(task_manager):
    filename = input("Enter filename to save tasks (e.g., tasks.csv): ")
    task_manager.save_task(filename)
    print(f"Tasks saved to {filename}.")

def load_tasks_from_csv(task_manager):
    filename = input("Enter filename to load tasks from (e.g., tasks.csv): ")
    task_manager.load_from_csv(filename)
    print(f"Tasks loaded from {filename}.")

def view_pending_and_overdue_tasks(task_manager):
    pending_tasks = task_manager.get_pending_tasks()
    overdue_tasks = task_manager.get_overdue_tasks()

    print("\nPending Tasks:")
    for task in pending_tasks:
        print(task)

    print("\nOverdue Tasks:")
    for task in overdue_tasks:
        print(task)

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. View Pending Tasks")
        print("7. View Overdue Tasks")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            task = create_task(task_manager)
            if task:
                task_manager.add_task(task)
                print("Task created successfully.")
        elif choice == "2":
            task_type = input("Enter task type (personal/work/all): ")
            tasks = task_manager.get_tasks(task_type.lower())
            if tasks:
                for task in tasks:
                    return task
            else:
                print("No tasks found.")
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "4":
            task_manager.save_task("task_list.csv")
            print("Tasks saved to task_list.csv.")
        elif choice == "5":
            task_manager.load_task("task_list.csv")
            print("Tasks loaded from task_list.csv.")
        elif choice == "6":
            pending_tasks = task_manager.get_pending_tasks()
            if pending_tasks:
                for task in pending_tasks:
                    print(task)
            else:
                print("No pending tasks.")
        elif choice == "7":
            overdue_tasks = task_manager.get_overdue_tasks()
            if overdue_tasks:
                for task in overdue_tasks:
                    print(task)
            else:
                print("No overdue tasks.")
        elif choice == "8":
            print("Exiting Task Management System... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()