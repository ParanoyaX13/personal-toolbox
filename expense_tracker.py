expenses = []

def add_expense():
    """Add a new expense"""
    
    name = input("Expense name: ").strip()
    
    try:
        amount = float(input("Expense amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    expenses.append({
        "name": name,
        "amount": amount
    })
    
    print("✅ Expense added successfully.")

def show_expenses():
    """Display all expenses"""
    
    if not expenses:
        print("No expenses recorded.")
        return
    
    total = 0
    
    print("\n=== Expense List ===")
    
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ${expense['amount']}")
        total += expense["amount"]
    
    print(f"\nTotal Expenses: ${total}")

def main():
    while True:
        print("\n=== Simple Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        print("4. Remove Expense")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
            elif choice == "4":
    
    if not expenses:
        print("No expenses to remove.")
        continue
    
    show_expenses()
    
    try:
        remove_index = int(input("Enter expense number to remove: "))
        
        removed = expenses.pop(remove_index - 1)
        
        print(f"✅ Removed: {removed['name']}")
    
    except (ValueError, IndexError):
        print("Invalid selection.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
