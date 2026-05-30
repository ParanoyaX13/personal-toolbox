import random

def love_calculator():
    """Fun Love Compatibility Calculator"""
    print("\n=== Love Calculator ❤️ ===")
    name1 = input("Enter first name: ").strip()
    name2 = input("Enter second name: ").strip()
    
    if not name1 or not name2:
        print("Please enter both names.")
        return
    
    # Simple fun calculation
    score = random.randint(60, 99)
    print(f"\n💕 Compatibility between {name1} and {name2}:")
    print(f"Love Score: {score}%")
    
    if score > 85:
        print("🔥 Perfect match! Soulmates!")
    elif score > 70:
        print("❤️ Great match! Very compatible.")
    elif score > 50:
        print("😊 Good potential.")
    else:
        print("💔 Maybe just friends...")

if __name__ == "__main__":
    love_calculator()
