"""Main module."""

import random
import string
import ipyleaflet

class Map(ipyleaflet.Map):
    
    def __init__(self, center=[20,0], zoom=2, **kwargs) -> None:

        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"] = True

        super().__init__(center=center, zoom=zoom,**kwargs)



    def add_search_control(self, position="topleft", **kwargs):

        search_control = ipyleaflet.SearchControl(**kwargs)
        self.add_control(search_control)





















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









def get_walks_starting_from(area, bridges=BRIDGES):
    walks = []

    def make_walks(area, walked=None, bridges_crossed=None):
        walked = walked or area
        bridges_crossed = bridges_crossed or ()
        available_bridges = [
            bridge 
            for bridge in bridges 
            if area in bridge and bridge not in bridges_crossed
        ]

        if not available_bridges:
            walks.append(walked)
            return
        
        for bridge in available_bridges:
            crossing = bridge[1:] if bridge[0] == area else bridge[1: -1]
            make_walks(
                area=crossing[-1], 
                walked=walked + crossing,
                bridges_crossed=(bridge, *bridges_crossed),
            )
    make_walks(area)
    return walks




