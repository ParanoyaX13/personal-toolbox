import random

def number_guessing_game():
    """Simple number guessing game"""
    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("📈 Too low! Try higher.")
            else:
                print("📉 Too high! Try lower.")
        except:
            print("Please enter a valid number.")
    
    print(f"😔 Game over! The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
