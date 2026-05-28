from datetime import datetime

tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False, "time": datetime.now().strftime("%H:%M")})
    print("Task added!")

def show_tasks():
    print("\n--- Your Todo List ---")
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⭕"
        print(f"{i}. {status} {t['task']} ({t['time']})")

def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        tasks[num]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid number!")

if __name__ == "__main__":
    print("Simple Todo List")
    while True:
        print("\n1. Add task | 2. Show tasks | 3. Mark done | 0. Exit")
        choice = input("Choose: ")
        if choice == "1": add_task()
        elif choice == "2": show_tasks()
        elif choice == "3": mark_done()
        elif choice == "0": break
