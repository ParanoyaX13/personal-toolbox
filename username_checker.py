taken_usernames = [
    "admin",
    "root",
    "test",
    "guest",
    "support",
    "developer"
]

def check_username():
    """Check username availability"""
    
    print("\n=== Username Availability Checker ===")
    
    username = input("Enter a username: ").strip().lower()
    
    if not username:
        print("Username cannot be empty.")
        return
        if len(username) < 4:
    print("❌ Username must be at least 4 characters long.")
    return
    
    if username in taken_usernames:
        print("❌ Username is already taken.")
    else:
        print("✅ Username is available.")

if __name__ == "__main__":
    check_username()
