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
    categories = {
    "1": "Motivation",
    "2": "Life",
    "3": "Coding"
}

print("\nSelect category:")
for k, v in categories.items():
    print(f"{k}. {v}")

choice = input("Choose category: ").strip()

filtered_quotes = quotes

if choice == "1":
    filtered_quotes = quotes[:3]
elif choice == "2":
    filtered_quotes = quotes[2:6]
elif choice == "3":
    filtered_quotes = quotes[4:]
else:
    filtered_quotes = quotes

quote = random.choice(filtered_quotes)
    
    print(f"\n💡 Quote:\n{quote}")

if __name__ == "__main__":
    generate_quote()
