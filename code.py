class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.show_tasks()
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                todo.complete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
