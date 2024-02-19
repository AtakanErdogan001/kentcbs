"""Main module."""

import random
import string

def generate_random_string(length=10):
    """Generate a random string of a given length.

    Args:
        length (int, optional): Length of the random string. Defaults to 10.

    Returns:
        _type_: Random string of the given length.
    """    
    # Define the pool of characters from which to choose
    characters = string.ascii_letters + string.digits + string.punctuation  # Include letters (both cases), digits, and punctuation
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

def lucky_number(length=3):
    """_summary_

    Args:
        length (int, optional): _description_. Defaults to 3.

    Returns:
        _type_: _description_.
    """    
    number = random.randint(0, 10**length - 1)
    
    return number