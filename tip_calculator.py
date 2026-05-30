def tip_calculator():
    """Restaurant Tip Calculator"""
    print("\n=== Tip Calculator ===")
    try:
        bill = float(input("Enter total bill amount: "))
        tip_percent = float(input("Tip percentage (10, 12, 15, 20): ") or 15)
        
        tip_amount = bill * (tip_percent / 100)
        total = bill + tip_amount
        
        print(f"\nTip Amount: {tip_amount:,.0f} IRR")
        print(f"Total Payment: {total:,.0f} IRR")
        
        people = int(input("Split between how many people? ") or 1)
        per_person = total / people
        print(f"Each person should pay: {per_person:,.0f} IRR")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    tip_calculator()
