def unit_price_calculator():
    """Calculate price per unit"""
    print("\n=== Unit Price Calculator ===")
    try:
        total_price = float(input("Enter total price: "))
        quantity = float(input("Enter quantity (e.g. kg, liter, piece): "))
        
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
            
        unit_price = total_price / quantity
        print(f"\nUnit Price: {unit_price:,.2f} per unit")
        print(f"For example: {unit_price:,.0f} IRR per kg/piece")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    unit_price_calculator()
