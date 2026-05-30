def word_counter():
    """Count words, characters, and sentences"""
    print("\n=== Word Counter 📝 ===")
    text = input("Enter your text:\n")
    
    words = len(text.split())
    characters = len(text)
    sentences = len([s for s in text.split('.') if s.strip()])
    
    print(f"\nResults:")
    print(f"• Words: {words}")
    print(f"• Characters: {characters}")
    print(f"• Sentences: {sentences}")
    print(f"• Average word length: {characters/words:.1f} if words > 0 else 0")

if __name__ == "__main__":
    word_counter()
