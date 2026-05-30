def is_leap_year(year):
    """Check if a year is leap year"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def leap_year_checker():
    print("\n=== Leap Year Checker 📅 ===")
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"✅ {year} is a Leap Year! (366 days)")
        else:
            print(f"❌ {year} is not a Leap Year.")
    except:
        print("Error: Please enter a valid year.")

if __name__ == "__main__":
    leap_year_checker()
