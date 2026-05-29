import random
import string
from utils import generate_password, get_current_time, validate_number

def show_menu():
    def show_menu():
    print("\n=== Personal Toolbox ===")
    print("1. Calculator")
    print("2. Password Generator")
    print("3. Unit Converter")
    print("4. Show Current Time")
    print("5. Currency Converter")
    print("6. File Organizer")        
    print("0. Exit")
    return input("Choose an option: ")
    in():
    print(f"Welcome! Current time: {get_current_time()}\n")
    while True:
        choice = show_menu()
     if choice == "1":
            calculator()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            unit_converter()
        elif choice == "4":
            print(f"Current time: {get_current_time()}")
        elif choice == "5":
            currency_converter()
        elif choice == "6":
            organize_files()
        elif choice == "0":
            print("Goodbye! Thanks for using Personal Toolbox.")
            break
        else:
            print("Invalid option. Try again.")
            lculator():
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
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        else:
            print("Invalid operation!")
            return
        print(f"Result: {num1} {operation} {num2} = {result}")
    except:
        print("Error: Please enter valid numbers.")

def password_generator():
    print("\n--- Strong Password Generator ---")
    try:
        length = int(input("Enter password length (min 8): ") or 12)
        if length < 8:
            length = 8
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, include_numbers, include_symbols)
        print(f"\nYour strong password: {password}")
    except:
        print("Error occurred.")

def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Back")
    
    choice = input("Choose: ")
    try:
        if choice == "1":
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km * 0.621371:.2f} miles")
        elif choice == "2":
            c = float(input("Enter Celsius: "))
            print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
        elif choice == "3":
            kg = float(input("Enter kilograms: "))
            print(f"{kg} kg = {kg * 2.20462:.2f} pounds")
    except:
        print("Error: Invalid input.")

if __name__ == "__main__":
    main()
