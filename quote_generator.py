import random

quotes = [
    "Stay hungry, stay foolish.",
    "Dream big and dare to fail.",
    "Simplicity is the ultimate sophistication.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Do something today that your future self will thank you for.",
    "Creativity is intelligence having fun.",
    "Small steps every day."
]

def generate_quote():
    """Display a random quote"""
    
    print("\n=== Random Quote Generator ===")
    
    quote = random.choice(quotes)
    
    print(f"\n💡 Quote:\n{quote}")

if __name__ == "__main__":
    generate_quote()
