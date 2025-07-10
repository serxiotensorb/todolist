import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Show [2] Add [3] Remove [4] Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
        elif choice == "3":
            show_tasks(tasks)
            idx = input("Enter task number to remove: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(tasks):
                removed = tasks.pop(int(idx) - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()