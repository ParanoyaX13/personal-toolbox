def loan_calculator():
    """Simple Loan / EMI Calculator"""
    print("\n=== Loan Calculator ===")
    try:
        principal = float(input("Enter loan amount (Principal): "))
        rate = float(input("Enter annual interest rate (%): ")) / 100
        months = int(input("Enter number of months: "))
        
        monthly_rate = rate / 12
        emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        
        print(f"\nMonthly Payment (EMI): {emi:,.0f} IRR")
        print(f"Total Payment: {(emi * months):,.0f} IRR")
        print(f"Total Interest: {(emi * months - principal):,.0f} IRR")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    loan_calculator()
