todo_list = []
print("===== Start a program =====")
while True:
    user_action = input("Enter a command (add, view, remove, exit): ")
    if user_action == "add":
        task = input("Enter a task to add: ")
        todo_list.append(task)
        print("Task added.")
    elif user_action == "view":
        if not todo_list:
            print("no tasks to display")
        else:
            print("##################################")
            counter = 1
        for task in todo_list:
            print(f"[{counter}] {task}")
            counter += 1
    elif user_action == "remove":
        if not todo_list:
            print("no tasks to remove")
        else:
            task = input("Enter a task to remove: ")
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
    elif user_action == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid command")
