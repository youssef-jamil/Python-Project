# to do List by using a chatGPT API
# # To do List:
import json
from datetime import datetime
import os


class Task:
    def __init__(self, title, description="", due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "completed": self.completed,
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["description"], data["due_date"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task


class TodoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")
        self.save_tasks()  # Save tasks after adding a new one

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task.completed else "✗"
            print(f"[{i}] {task.title} - {status} - Created at: {task.created_at}")
            if task.description:
                print(f"   Description: {task.description}")
            if task.due_date:
                print(f"   Due date: {task.due_date}")
            print("=================================")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(
                f"The task '{self.tasks[task_index].title}' has been marked as completed."
            )
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task_title = self.tasks[task_index].title
            self.tasks.remove(self.tasks[task_index])
            print(f"The task '{task_title}' has been removed.")
        else:
            print("Invalid task index.")

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in self.tasks],
                file,
                ensure_ascii=False,
                indent=4,
            )
            print("Tasks saved to file.")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]
                print("Tasks loaded from file.")
        else:
            print("No saved tasks found. Starting with an empty task list.")


def main():
    todo = TodoList()

    while True:
        print("===== Start a program =====")
        print("\n The list of commands:")
        print("1. add - Add a task")
        print("2. view - View all tasks")
        print("3. remove - Remove a task")
        print("4. mark - Mark a task as completed")
        print("5. save - Save tasks to file")
        print("6. exit - Exit the program")

        user_choice = input("Enter a number to choose an option(1-6): ")

        if user_choice == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description (optional): ")
            due_date = input("Enter the due date (optional): ")
            todo.add_task(Task(title, description, due_date))
        elif user_choice == "2":
            todo.view_tasks()
        elif user_choice == "3":
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo.remove_task(task_index)
        elif user_choice == "4":
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo.mark_completed(task_index)
        elif user_choice == "5":
            todo.save_tasks()
        elif user_choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
