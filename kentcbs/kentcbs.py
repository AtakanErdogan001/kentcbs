"""Main module."""

import random
import string
import ipyleaflet
import pandas as pd
import selenium

class Map(ipyleaflet.Map):
    
    def __init__(self, center=[20,0], zoom=2, **kwargs) -> None:

        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"] = True

        super().__init__(center=center, zoom=zoom,**kwargs)



    def add_search_control(self, position="topleft", **kwargs):

        search_control = ipyleaflet.SearchControl(**kwargs)
        self.add_control(search_control)


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

class Meteorology():
def __init__(self, path, url):

    self.path = path
    self.url = url
    self.browser = webdriver.Chrome(self.path)
    self.browser.get(self.url)

    def get_xy(self, sehirler):
        result_xy_list = []
        for il in sehirler:
            sayi = 1
            xpath = f"/html/body/div[3]/div/div/div/div/div/div[1]/select/option[text()='{il}']"
            self.browser.find_element(By.XPATH, xpath).click()

            # check
            act_title = self.browser.title
            exp_title = "İstasyon Bilgileri Veritabanı - Meteoroloji Genel Müdürlüğü" 
            if act_title == exp_title:
                print("Passed")
            else:
                print("Failed")
            # wait for response
            time.sleep(3)

            # get link
            loops = self.browser.find_elements(By.XPATH, '//*[@id="ayrinti"]/table/tbody/tr/td/a')

            # split/rearrange x-y
            for loop in loops:
                # Find the district element associated with the station
                ilce_element = self.browser.find_elements(By.XPATH, f'//*[@id="ayrinti"]/table/tbody/tr[{sayi}]/td[5]')
                ilce_text_list = [ilce.text for ilce in ilce_element if ilce.text.strip()]
                print(f"Ilce text list for {il}: {ilce_text_list}")

                # Find the station number element associated with the station
                station_no_element = self.browser.find_elements(By.XPATH, f'//*[@id="ayrinti"]/table/tbody/tr[{sayi}]/td[3]')
                station_no_text = station_no_element[0].text if station_no_element else ""
                print(f"Station number for {il}: {station_no_text}")

                # Extract X and Y coordinates
                loop_1 = loop.get_attribute('href')
                result_1 = loop_1.split('=', 2)[2]
                result_x, result_y = result_1.split(',', 1)

                # Append data to the result list
                result_xy_list.append([il, ", ".join(ilce_text_list), station_no_text, result_x, result_y])

                # Increment sayi for the next iteration
                sayi += 1

        # export
        print(result_xy_list)






















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




