import os 

#file to store tasks
file_name= "tasks.txt"

def load_tasks():
    tasks={}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                task_id,  title, status = line.strip().split("|")
                tasks[int(task_id)] = {
                    "title": title,
                    "status": status
                }
    return tasks

#save tasks to file

def save_tasks(tasks):
    with open(file_name, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id}|{task['title']}|{task['status']}\n")

#add a new task
def add_task(tasks):
    title= input("Enter task title: ")
    tasks_id = max(tasks.keys(), default=0) + 1  # Get the next task ID
    tasks[tasks_id] = {
        "title": title,
        "status": "pending"
    }
    print(f"Task '{title}' added with ID {tasks_id}.")

#view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")

#update a task
def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    if task_id in tasks:
        tasks[task_id] ["status"]= "completed"
        print(f"Task '{tasks[task_id]['title']}' completed.")
    else:
        print(f"Task with ID {task_id} not found.")


#delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_tasks = tasks.pop(task_id)
        print(f"Task '{tasks[task_id]['title']}' deleted.")
    else:
        print(f"Task with ID {task_id} not found.")


#main function to run the task manager
def main():
    tasks=load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()