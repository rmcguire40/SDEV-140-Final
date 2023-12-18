import urllib.request
import urllib.parse
import json

from .utils import cprint, colors
from ._meta import TEST_CITIES

def get_coordinates_test():
    """Run a test on the subsystem that converts city names to coordinates.
    """

    # Get the keys from the TEST_CITIES dictionary
    keys = TEST_CITIES

    cprint("Running get_coordinates_test", colors.bold)

    for key in keys:
        try:
            # get the coords and compare with our test data
            coords = get_coordinates(key)
            assert coords == keys[key]
            cprint(f"Test passed for {key}", colors.green)

        except Exception as e:
            # so we know what went wrong
            exception_desc = str(e)
            cprint(f"Test failed for {key}", colors.red)
            
            if isinstance(e, ValueError):  # this generally means the city name was not found
                cprint(f"This is likely because the city name was not found ({exception_desc})", colors.yellow)
            
            elif isinstance(e, urllib.error.URLError):  # this generally means there was an internet error, or the API is down
                cprint(f"This is likely because there was an http or internet error ({exception_desc})", colors.yellow)
            
            elif isinstance(e, AssertionError):  # this is the best error to get cause it means the coords were wrong
                cprint(f"Expected ({keys[key]}) - Got ({coords})", colors.yellow)
            
            else:
                cprint(f"Unknown error ({exception_desc})", colors.yellow)

    cprint("Finished get_coordinates_test", colors.bold)

def get_coordinates(city_name):
    """This function uses a publicly available API to get the coordinates of a city or location using 
    openstreetmap.org. The function takes a city name as input and returns a tuple of latitude and longitude
    coordinates. If the city name is not found, the function raises a ValueError, if there's an http or internet error,
    it will raise urllib.error.URLError.

    Args:
        city_name (str): The name of the city to get the coordinates of

    Raises:
        ValueError: If the city name is not found
        urllib.error.URLError: If there's an http or internet error

    Returns:
        tuple(float, float): A tuple of latitude and longitude coordinates, should be piped to another service to fetch weather
    """

    # URL encode the city name
    city_name_encoded = urllib.parse.quote_plus(city_name)

    # Define the URL for the API request
    url = f"https://nominatim.openstreetmap.org/search?q={city_name_encoded}&format=json"

    # Make the request and read the response
    with urllib.request.urlopen(url) as response:
        if data := json.loads(response.read().decode()):
            return float(data[0]["lat"]), float(data[0]["lon"])
        print(data)
        raise ValueError(f"Failed to find coordinates for {city_name}")
