import random

def roll_dice():
    """Simulate dice rolling"""
    
    print("\n=== Dice Simulator ===")
    
    dice = input("How many dice to roll? ").strip()
    rounds = input("How many rounds? (default 1): ").strip()

try:
    rounds = int(rounds) if rounds else 1
except ValueError:
    rounds = 1
    
    try:
        dice = int(dice)
    except ValueError:
        print("Invalid number.")
        return
    
    all_rounds = []

for r in range(rounds):
    results = []
    
    for _ in range(dice):
        results.append(random.randint(1, 6))
    
    all_rounds.append(results)
    
    print(f"Round {r+1}: {results} | Total: {sum(results)}")
    
    for _ in range(dice):
        results.append(random.randint(1, 6))
    
    print(f"\n🎲 Results: {results}")
    print(f"Dice Rolled: {len(results)}")
    print(f"Total: {sum(results)}")
    ones = results.count(1)
print(f"Number of ones: {ones}")
    sixes = results.count(6)
print(f"Number of sixes: {sixes}")
    print(f"Average Roll: {sum(results) / len(results):.2f}")
    print(f"Highest Roll: {max(results)}")
    print(f"Lowest Roll: {min(results)}")

if __name__ == "__main__":
    roll_dice()
    print("\n🎲 Finished all rounds.")
