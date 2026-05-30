def binary_converter():
    """Convert between Binary and Decimal"""
    print("\n=== Binary ↔ Decimal Converter ===")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    
    choice = input("Choose (1 or 2): ")
    
    try:
        if choice == "1":
            num = int(input("Enter decimal number: "))
            print(f"Binary: {bin(num)[2:]}")
        elif choice == "2":
            binary = input("Enter binary number: ")
            print(f"Decimal: {int(binary, 2)}")
        else:
            print("Invalid choice!")
    except:
        print("Error: Invalid input.")

if __name__ == "__main__":
    binary_converter()
