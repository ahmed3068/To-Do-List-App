def display_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")
    return input("Enter your choice: ")

def main():
    print("Welcome to the To-Do List App!")
    tasks = []

    while True:
        choice = display_menu()

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            if tasks:
                for i, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{i + 1}. {task['task']} - {status}")
            else:
                print("No tasks added yet.")

        elif choice == '3':
            if tasks:
                try:
                    task_num = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["done"] = True
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks available to mark as done.")

        elif choice == '4':
            if tasks:
                try:
                    task_num = int(input("Enter the task number to remove: ")) - 1
                    if 0 <= task_num < len(tasks):
                        removed = tasks.pop(task_num)
                        print(f"Task '{removed['task']}' removed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks available to remove.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
