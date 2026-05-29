import random

def roll_dice():
    """Simulate dice rolling"""
    
    print("\n=== Dice Simulator ===")
    
    dice = input("How many dice to roll? ").strip()
    
    try:
        dice = int(dice)
    except ValueError:
        print("Invalid number.")
        return
    
    results = []
    
    for _ in range(dice):
        results.append(random.randint(1, 6))
    
    print(f"\n🎲 Results: {results}")
    print(f"Total: {sum(results)}")

if __name__ == "__main__":
    roll_dice()
