def convert_length():
    """Convert meters to other units"""
    
    meters = float(input("Enter value in meters: "))
    
    print("\nSelect conversion:")
    print("1. Meters to Kilometers")
    print("2. Meters to Centimeters")
    print("3. Meters to Millimeters")
    print("4. Kilometers to Miles")
    choice = input("Choose option: ").strip()
    
    if choice == "1":
        print(f"{meters} m = {meters / 1000} km")
    elif choice == "2":
        print(f"{meters} m = {meters * 100} cm")
    elif choice == "3":
        print(f"{meters} m = {meters * 1000} mm")
    elif choice == "4":
    km = meters / 1000
    print(f"{km} km = {km * 0.621371} miles")    
    else:
        print("Invalid option.")

if __name__ == "__main__":
    print("=== Unit Converter ===")
    convert_length()
