"""Main module."""

import random
import string

def generate_random_string(length=10):
    # Define the pool of characters from which to choose
    characters = string.ascii_letters + string.digits + string.punctuation  # Include letters (both cases), digits, and punctuation
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

def lucky_number(length=3):
    # Generate a random number
    number = random.randint(0, 10**length - 1)
    
    return number