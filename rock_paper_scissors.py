import random

def rock_paper_scissors():
    """Classic Rock Paper Scissors game"""
    print("\n=== Rock Paper Scissors ===")
    print("1. Rock\n2. Paper\n3. Scissors\n0. Quit")
    
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        user_choice = input("\nYour choice (1-3 or 0): ")
        if user_choice == "0":
            print("Thanks for playing!")
            break
        
        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice!")
            continue
            
        user_move = choices[int(user_choice)-1]
        computer_move = random.choice(choices)
        
        print(f"You played: {user_move}")
        print(f"Computer played: {computer_move}")
        
        if user_move == computer_move:
            print("🤝 It's a tie!")
        elif (user_move == "Rock" and computer_move == "Scissors") or \
             (user_move == "Paper" and computer_move == "Rock") or \
             (user_move == "Scissors" and computer_move == "Paper"):
            print("🎉 You Win!")
        else:
            print("😔 You Lose!")

if __name__ == "__main__":
    rock_paper_scissors()
