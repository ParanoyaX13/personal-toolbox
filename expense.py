def expense_tracker():
    """Simple daily expense tracker"""
    print("\n=== Expense Tracker ===")
    expenses = []
    total = 0
    
    print("Enter your expenses (type 'done' to finish):")
    
    while True:
        item = input("Expense name (or 'done'): ")
        if item.lower() == 'done':
            break
        try:
            amount = float(input("Amount (in IRR): "))
            expenses.append((item, amount))
            total += amount
            print(f"✅ Added: {item} - {amount:,} IRR")
        except:
            print("Invalid amount.")
    
    print(f"\n📊 Total Expenses: {total:,} IRR")
    if total > 0:
        print("\nSummary:")
        for item, amount in expenses:
            print(f"• {item}: {amount:,} IRR")

if __name__ == "__main__":
    expense_tracker()
