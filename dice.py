import random

def roll_dice():
    """Roll dice simulator"""
    print("\n=== Dice Roller 🎲 ===")
    try:
        num_dice = int(input("How many dice do you want to roll? (1-10): ") or 1)
        sides = int(input("How many sides? (default 6): ") or 6)
        
        if num_dice < 1 or num_dice > 10:
            num_dice = 1
        if sides < 2:
            sides = 6
            
        print(f"\nRolling {num_dice} dice with {sides} sides...")
        results = [random.randint(1, sides) for _ in range(num_dice)]
        
        for i, result in enumerate(results, 1):
            print(f"Dice {i}: 🎲 {result}")
        
        print(f"\nTotal: {sum(results)}")
    except:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    roll_dice()
