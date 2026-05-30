import string

def check_password(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"

def main():
    print("\n=== Password Checker ===")
    password = input("Enter password: ")
    
    result = check_password(password)
    print(f"Strength: {result}")

if __name__ == "__main__":
    main()
