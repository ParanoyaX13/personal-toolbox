import random

def tell_joke():
    """Tell a random funny joke"""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the Python programmer quit his job? He didn't like the indentation pressure.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "Debugging: Being the detective in a crime movie where you are also the murderer.",
        "There are 10 types of people in the world: Those who understand binary and those who don't.",
        "Why was the JavaScript developer sad? He didn't know how to 'null' his feelings."
    ]
    
    print("\n=== Joke Teller ===")
    joke = random.choice(jokes)
    print(f"😂 {joke}")
    print("\nHope that made you smile! 😄")

if __name__ == "__main__":
    tell_joke()
