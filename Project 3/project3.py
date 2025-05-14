# To do List:
tasks = []
while True:
    print("===== Start a program =====")
    print("======= To Do List ========")
    user_command = input("Enter a command (add, view, remove, exit): ")
    if user_command == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif user_command == "view":
        if not tasks:
            print("No tasks to display.")
        else:
            print("=================================")
            for task in tasks:
                print(task)
    elif user_command == "remove":
        if not tasks:
            print("No tasks to remove.")
        else:
            task = input("Enter a task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
    elif user_command == "exit":
        break
    else:
        print("Invalid command")
