def calculator():
    """Simple CLI calculator"""
    
    print("\n=== Simple Calculator ===")
    
    num1 = float(input("Enter first number: "))
    op = input("Choose operator (+, -, *, /): ").strip()
    num2 = float(input("Enter second number: "))
    
    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid operator.")

if __name__ == "__main__":
    calculator()
