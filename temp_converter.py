def temperature_converter():
    """Temperature Converter (Celsius, Fahrenheit, Kelvin)"""
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("Choose (1-3): ")
    try:
        if choice == "1":
            c = float(input("Enter Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C = {f:.2f}°F")
        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}°F = {c:.2f}°C")
        elif choice == "3":
            c = float(input("Enter Celsius: "))
            k = c + 273.15
            print(f"{c}°C = {k:.2f} K")
        else:
            print("Invalid choice!")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    temperature_converter()
