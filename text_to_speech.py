def text_to_speech_simulator():
    """Simple text-to-speech simulator"""
    print("\n=== Text to Speech Simulator ===")
    text = input("Enter text you want to 'speak': ").strip()
    
    if not text:
        print("No text entered.")
        return
    
    print(f"\n🔊 Speaking: \"{text}\"")
    print("🎙️  (Imagine this is being spoken out loud)")
    
    # Simulate speaking speed
    words = text.split()
    for word in words:
        print(word, end=" ", flush=True)
        # Small delay simulation
        import time
        time.sleep(0.15)
    
    print("\n\n✅ Speech completed!")

if __name__ == "__main__":
    text_to_speech_simulator()
