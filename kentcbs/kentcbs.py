"""Main module."""

import random
import string
import ipyleaflet

class Map(ipyleaflet.Map):
    
    def __init__(self, center=[20,0], zoom=2, **kwargs) -> None:

        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"] = True

        super().__init__(center=center, zoom=zoom,**kwargs)

        if "layer_control" not in kwargs:
           kwargs["layer_control"] = True
        
        if kwargs["search_control"]:    
           self.add_layers_control()



    def add_search_control(self, position="topleft", **kwargs):
        """_summary_

        Args:
            position (str, optional): _description_. Defaults to "topleft".
        """
        if "url" not in kwargs:
            kwargs["url"] = "https://nominatim.openstreetmap.org/search?format=json&q={s}"

        search_control = ipyleaflet.SearchControl(position=position,**kwargs)
        self.add_control(search_control)

    def add_draw_control(self, position="topleft", **kwargs):
        """_summary_

        Args:
            position (str, optional): _description_. Defaults to "topleft".
        """
        draw_control = ipyleaflet.DrawControl(position=position,**kwargs)
        self.add_control(draw_control)
        """_summary_
        """
        draw_control.polyline = {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
            }
        }
        draw_control.polygon = {
            "shapeOptions": {
                "fillColor": "#6be5c3",
                "color": "#6be5c3",
                "fillOpacity": 1.0
            },
            "drawError": {
                "color": "#dd253b",
                "message": "Oups!"
            },
            "allowIntersection": False
        }
        draw_control.circle = {
            "shapeOptions": {
                "fillColor": "#efed69",
                "color": "#efed69",
                "fillOpacity": 1.0
            }
        }
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 1.0
            }
        }

        self.add_control(draw_control)

        

    
    def add_layers_control(self, position='topright',**kwargs):

        layers_control = ipyleaflet.LayersControl(position=position,**kwargs)
        self.add_control(layers_control)






















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
                bridges_crossed=(bridge, *bridge_crossed),
            )
    make_walks(area)
    return walks

