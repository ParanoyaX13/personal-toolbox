import random

def random_fact():
    """Display a random interesting fact"""
    facts = [
        "Octopuses have three hearts and blue blood.",
        "A day on Venus is longer than a year on Venus.",
        "Honey never spoils. Archaeologists found 3000-year-old honey that was still edible.",
        "The first computer bug was literally a moth stuck in the machine.",
        "Bananas are technically berries, but strawberries aren't.",
        "The Python programming language was named after Monty Python, not the snake.",
        "There are more possible games of chess than atoms in the observable universe."
    ]
    
    print("\n=== Random Fact Generator ===")
    fact = random.choice(facts)
    print(f"🧠 Did you know?\n{fact}")
    print("\nKnowledge is power! 📚")

if __name__ == "__main__":
    random_fact()
