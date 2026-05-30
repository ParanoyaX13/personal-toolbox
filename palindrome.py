def is_palindrome(text):
    """Check if a word or sentence is palindrome"""
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

def palindrome_checker():
    """Palindrome Checker Tool"""
    print("\n=== Palindrome Checker ===")
    text = input("Enter a word or sentence: ").strip()
    
    if is_palindrome(text):
        print(f"✅ \"{text}\" is a Palindrome!")
    else:
        print(f"❌ \"{text}\" is not a Palindrome.")

if __name__ == "__main__":
    palindrome_checker()
