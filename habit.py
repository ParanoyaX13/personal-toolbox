def habit_tracker():
    """Simple daily habit tracker"""
    print("\n=== Daily Habit Tracker ===")
    habits = ["Exercise", "Read 10 pages", "Drink 8 glasses of water", "Meditate", "Code for 30 minutes"]
    
    print("Track your today's habits:")
    completed = 0
    
    for i, habit in enumerate(habits, 1):
        done = input(f"{i}. {habit}? (y/n): ").lower() == 'y'
        if done:
            completed += 1
            print("   ✅ Done")
        else:
            print("   ⭕ Not done")
    
    percentage = (completed / len(habits)) * 100
    print(f"\nToday's progress: {completed}/{len(habits)} ({percentage:.0f}%)")
    
    if percentage == 100:
        print("🎉 Perfect day! Keep the streak alive!")
    elif percentage >= 70:
        print("👍 Good job! You're doing great.")
    else:
        print("💪 Tomorrow is another chance. Don't give up!")

if __name__ == "__main__":
    habit_tracker()
