import random
import string

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
    print("\n--- Strong Password Generator ---")
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            length = 8
            print("Minimum length set to 8.")
        
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        characters = string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"\nYour generated password: {password}")
    except:
        print("Error: Please enter a valid number.")

def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Back to menu")
    
    choice = input("Choose conversion type: ")
    
    try:
        if choice == "1":
            km = float(input("Enter kilometers: "))
            miles = km * 0.621371
            print(f"{km} km = {miles:.2f} miles")
        elif choice == "2":
            celsius = float(input("Enter Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        elif choice == "3":
            kg = float(input("Enter kilograms: "))
            pounds = kg * 2.20462
            print(f"{kg} kg = {pounds:.2f} pounds")
        elif choice == "4":
            return
        else:
            print("Invalid choice!")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
