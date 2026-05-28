def show_menu():
    print("\n=== Personal Toolbox ===")
    print("1. Calculator")
    print("2. Password Generator")
    print("3. Unit Converter")
    print("0. Exit")
    return input("Choose an option: ")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            calculator()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            unit_converter()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def calculator():
    print("\n--- Advanced Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("Invalid operation!")
            return
        
        print(f"Result: {num1} {operation} {num2} = {result}")
    except:
        print("Error: Please enter valid numbers.")

def password_generator():
    print("Password Generator - Coming soon...")

def unit_converter():
    print("Unit Converter - Coming soon...")

if __name__ == "__main__":
    main()
