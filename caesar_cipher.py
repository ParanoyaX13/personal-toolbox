def caesar_cipher(text, shift, encrypt=True):
    """Simple Caesar Cipher encryption/decryption"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + (shift if encrypt else -shift)) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + (shift if encrypt else -shift)) % 26 + 97)
        else:
            result += char
    return result

def caesar_tool():
    """Caesar Cipher Tool"""
    print("\n=== Caesar Cipher Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Choose (1 or 2): ")
    text = input("Enter text: ")
    shift = int(input("Enter shift number (1-25): "))
    
    if choice == "1":
        result = caesar_cipher(text, shift, encrypt=True)
        print(f"🔒 Encrypted: {result}")
    elif choice == "2":
        result = caesar_cipher(text, shift, encrypt=False)
        print(f"🔓 Decrypted: {result}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    caesar_tool()
