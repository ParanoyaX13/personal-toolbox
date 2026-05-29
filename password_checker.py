import re

def check_password_strength(password):
    """Check the strength of a password"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")
    
    return score, feedback

def password_strength_checker():
    print("\n=== Password Strength Checker ===")
    password = input("Enter a password to check: ")
    
    score, feedback = check_password_strength(password)
    
    print(f"\nStrength Score: {score}/5")
    
    if score == 5:
        print("✅ Excellent! Very strong password.")
    elif score >= 4:
        print("🟡 Good password.")
    elif score >= 3:
        print("🟠 Medium strength.")
    else:
        print("🔴 Weak password.")
    
    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    password_strength_checker()
