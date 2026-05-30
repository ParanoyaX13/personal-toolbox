def speed_converter():
    """Convert between different speed units"""
    print("\n=== Speed Converter ===")
    print("1. km/h to mph")
    print("2. mph to km/h")
    
    choice = input("Choose (1 or 2): ")
    try:
        if choice == "1":
            kmh = float(input("Enter speed in km/h: "))
            mph = kmh * 0.621371
            print(f"{kmh} km/h = {mph:.2f} mph")
        elif choice == "2":
            mph = float(input("Enter speed in mph: "))
            kmh = mph * 1.60934
            print(f"{mph} mph = {kmh:.2f} km/h")
        else:
            print("Invalid choice!")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    speed_converter()
