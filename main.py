"""
Personal Toolbox - Main Application
A collection of useful command-line tools.

Author: ParanoyaX13
Version: 1.0
Created: May 2026
"""

from datetime import datetime
from utils import generate_password, get_current_time
from organizer import organize_files
from weather import get_weather
from game import number_guessing_game
from password_checker import password_strength_checker
from bmi import bmi_calculator
from rock_paper_scissors import rock_paper_scissors
from age_calculator import age_calculator
from quotes import motivational_quote
from timer import countdown_timer
from habit import habit_tracker



def show_menu():
    """Display the main menu and return user's choice"""
    print("\n=== Personal Toolbox ===")
    print("1. Calculator")
    print("2. Password Generator")
    print("3. Unit Converter")
    print("4. Show Current Time")
    print("5. Currency Converter")
    print("6. File Organizer")
    print("7. Weather Simulator")
    print("8. Number Guessing Game") 
    print("9. Password Strength Checker")
    print("10. BMI Calculator")
    print("11. Rock Paper Scissors") 
    print("12. Age Calculator")
    print("13. Motivational Quote")
    print("14. Countdown Timer")
    print("15. Habit Tracker") 
    print("0. Exit")
    return input("Choose an option: ")


def main():
    """Main application loop that handles user navigation"""
    print(f"Welcome to Personal Toolbox! Current time: {get_current_time()}\n")
    
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
            elif choice == "7":           
            get_weather()
        elif choice == "8":                    
            number_guessing_game()
    elif choice == "9":                       
            password_strength_checker()
elif choice == "10":                  
            bmi_calculator()
elif choice == "11":                     
            rock_paper_scissors()
elif choice == "12":                     
            age_calculator()
elif choice == "13":                    
            motivational_quote()
    elif choice == "14":                     
            countdown_timer()
elif choice == "15":                     
            habit_tracker()
        elif choice == "0":
            print("Goodbye! Thanks for using Personal Toolbox.")
            break
        else:
            print("Invalid option. Try again.")


def calculator():
    """Advanced calculator supporting basic arithmetic operations"""
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
    """Generates strong random passwords with user preferences"""
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
    """Converts between different units (length, temperature, weight)"""
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


def currency_converter():
    """Converts Iranian Rial to other currencies (demo rates)"""
    print("\n--- Currency Converter (Mock) ---")
    print("Note: This is a demo version with fixed rates.")
    try:
        amount = float(input("Enter amount in IRR: "))
        print(f"\n{amount:,} IRR")
        print(f"≈ {amount/42000:.2f} USD")
        print(f"≈ {amount/48000:.2f} EUR")
        print(f"≈ {amount/55000:.2f} GBP")
        print(f"≈ {amount/12:.0f} AED")
    except:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
