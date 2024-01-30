# Define ToDoList class, add, delete and view functions
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task} added successfully.")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task {task} removed successfully.")
        else:
            print(f"Task {task} not found!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list!")
        else:
            print("---My To-Do List---\n")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

# Usage
todo_list = ToDoList()

while True:
    print("Choose one of the options below.")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter option: ")

    if choice == "1":
        # Ask for user to add task
        task = input("Add task: ")
        todo_list.add_task(task)

    elif choice == "2":
        # Ask for user to delete task
        task = input("Delete task: ")
        todo_list.delete_task(task)

    elif choice == "3":
        # View tasks
        todo_list.view_tasks()

    elif choice == "4":
        print("Exiting the To-Do List. Have a nice day!")
        break

    else:
        print("Invalid choice! Please try again")