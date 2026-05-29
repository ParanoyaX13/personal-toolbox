import time

def countdown_timer():
    """Simple countdown timer"""
    print("\n=== Countdown Timer ===")
    try:
        seconds = int(input("Enter time in seconds: "))
        if seconds <= 0:
            print("Please enter a positive number.")
            return
            
        print(f"Starting countdown from {seconds} seconds...")
        
        for i in range(seconds, 0, -1):
            print(f"⏳ {i} seconds remaining", end="\r")
            time.sleep(1)
        
        print("\n\n🎉 Time's up! Timer finished!")
    except:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    countdown_timer()
