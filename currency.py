def currency_converter():
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
    currency_converter()
