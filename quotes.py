import random

def motivational_quote():
    """Display a random motivational quote"""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "It always seems impossible until it's done. - Nelson Mandela",
        "Success is not final, failure is not fatal. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Don't watch the clock; do what it does. Keep going.",
        "Everything you’ve ever wanted is sitting on the other side of fear.",
        "Your only limit is you.",
        "Small daily improvements are the key to staggering long-term results."
    ]
    
    print("\n=== Motivational Quote Generator ===")
    quote = random.choice(quotes)
    print(f"💡 \"{quote}\"")
    print("\nKeep going! You're doing great 🚀")

if __name__ == "__main__":
    motivational_quote()
