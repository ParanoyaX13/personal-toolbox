def roll_dice():
    """Simulate dice rolling"""
    
    print("\n=== Dice Simulator ===")
    
    dice = input("How many dice to roll? ").strip()
    
    try:
        dice = int(dice)
    except ValueError:
        print("Invalid number.")
        return

    rounds = input("How many rounds? (default 1): ").strip()

    try:
        rounds = int(rounds) if rounds else 1
    except ValueError:
        rounds = 1

    all_rounds = []

    for r in range(rounds):
        results = []
        
        for _ in range(dice):
            results.append(random.randint(1, 6))
        
        all_rounds.append(results)
        
        print(f"\nRound {r+1}: {results}")
        print(f"Total: {sum(results)}")
        print(f"Highest Roll: {max(results)}")
        print(f"Lowest Roll: {min(results)}")
        print(f"Average Roll: {sum(results) / len(results):.2f}")
        print(f"Number of sixes: {results.count(6)}")
        print(f"Number of ones: {results.count(1)}")
        print(f"Dice Rolled: {len(results)}")
        print(f"Sorted Results: {sorted(results)}")
        
        if all(value == 6 for value in results):
            print("🔥 JACKPOT! All dice landed on 6!")

    print("\n🎲 Finished all rounds.")

    all_rounds.clear()
