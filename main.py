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
    print("Calculator - Coming soon...")

def password_generator():
    print("Password Generator - Coming soon...")

def unit_converter():
    print("Unit Converter - Coming soon...")

if __name__ == "__main__":
    main()
