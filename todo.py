class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def mark_as_done(self):
        self.done = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task.done else "Not Done"
                print(f"{i}. {task.description} - {status}")

    def mark_task_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_as_done()
            print("Task marked as done.")
        else:
            print("Task number does not exist.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted.")
        else:
            print("Task number does not exist.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            task = Task(task_description)
            todo_list.add_task(task)
            print("Task added.")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as done: "))
            todo_list.mark_task_done(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()