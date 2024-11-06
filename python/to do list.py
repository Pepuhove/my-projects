import os

class TodoList:
    def __init__(self, file_path="todo.txt"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully.")

    def update_task(self, task_number, new_task):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1] = new_task
            self.save_tasks()
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.show_tasks()

        elif choice == "2":
            new_task = input("Enter the new task: ")
            todo_list.add_task(new_task)

        elif choice == "3":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the updated task: ")
            todo_list.update_task(task_number, new_task)

        elif choice == "4":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_number)

        elif choice == "5":
            print("Exiting To-Do List.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
