todos = []

def show_todos():
    if not todos:
        print("No tasks yet.")
        return
    
    print("\n=== To-Do List ===")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        todos.append(task)
        print("Task added.")

def remove_task():
    show_todos()
    try:
        index = int(input("Task number to remove: "))
        removed = todos.pop(index - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid selection.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_todos()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
