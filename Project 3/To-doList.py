import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
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
            "completed": self.completed,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["description"], data["due_date"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.filename = "tasks.json"
        self.tasks = []

        # واجهة المستخدم
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack()

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(fill="x")

        self.complete_button = tk.Button(
            self.frame, text="Mark Completed", command=self.mark_completed
        )
        self.complete_button.pack(fill="x")

        self.remove_button = tk.Button(
            self.frame, text="Remove Task", command=self.remove_task
        )
        self.remove_button.pack(fill="x")

        self.save_button = tk.Button(
            self.frame, text="Save Tasks", command=self.save_tasks
        )
        self.save_button.pack(fill="x")

        self.load_tasks()

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter the task title:")
        if not title:
            return

        description = simpledialog.askstring(
            "Task Description", "Enter task description (optional):"
        )
        due_date = simpledialog.askstring("Due Date", "Enter due date (optional):")

        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.update_listbox()

    def mark_completed(self):
        if selected := self.listbox.curselection():
            index = selected[0]
            self.tasks[index].completed = True
            self.update_listbox()
        else:
            messagebox.showwarning(
                "No Selection", "Please select a task to mark as completed."
            )

    def remove_task(self):
        if selected := self.listbox.curselection():
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("No Selection", "Please select a task to remove.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            display = f"{task.title} [{status}]"
            self.listbox.insert(tk.END, display)

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in self.tasks],
                file,
                ensure_ascii=False,
                indent=4,
            )
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(item) for item in data]
                    self.update_listbox()
            except json.JSONDecodeError:
                messagebox.showwarning(
                    "Error", "Could not load tasks. File might be corrupted."
                )


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
