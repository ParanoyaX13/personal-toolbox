import random
import string
from datetime import datetime

def generate_password(length=12, include_numbers=True, include_symbols=True):
    """Generate a strong random password"""
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_current_time():
    """Return current date and time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_number(input_str):
    """Validate if string is a valid number"""
    try:
        return float(input_str)
    except ValueError:
        return None
