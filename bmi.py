def bmi_calculator():
    """Body Mass Index Calculator"""
    print("\n=== BMI Calculator ===")
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (meters): "))
        
        if height <= 0:
            print("Height must be greater than zero.")
            return
            
        bmi = weight / (height ** 2)
        print(f"\nYour BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
            
        print("\nTip: A healthy BMI is between 18.5 and 24.9")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    bmi_calculator()
