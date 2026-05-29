from datetime import datetime

def age_calculator():
    """Calculate age based on birth year"""
    print("\n=== Age Calculator ===")
    try:
        birth_year = int(input("Enter your birth year (e.g. 2000): "))
        current_year = datetime.now().year
        
        age = current_year - birth_year
        print(f"\nYou are approximately {age} years old.")
        
        if age < 18:
            print("You're still young! Enjoy your time.")
        elif age < 30:
            print("You're in your prime years!")
        elif age < 50:
            print("Middle age vibes 😎")
        else:
            print("Wisdom comes with age ✨")
    except:
        print("Error: Please enter a valid year.")

if __name__ == "__main__":
    age_calculator()
