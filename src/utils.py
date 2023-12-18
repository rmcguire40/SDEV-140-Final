from .weathercodes import CODES
import os

class colors:
    """This is just a class that contains some ANSI escape codes for colors and formatting, not windows compatible
    """
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    end = '\033[0m'
    
def cprint(text, color):
    """This function prints text in color, it's not windows compatible either"""
    print(f"{color}{text}{colors.end}")

def celsius_to_fahrenheit(celsius, round_result=True):
    """Converts celsius to fahrenheit for temperature conversion

    Args:
        celsius (float, int): The temperature in celsius
        round_result (bool, optional): Whether or not to round the result. Defaults to True.

    Returns:
        float: The temperature in fahrenheit
    """
    return round(celsius * 9/5 + 32) if round else celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit, round_result=True):
    """Converts fahrenheit to celsius for temperature conversion

    Args:
        fahrenheit (float, int): The temperature in fahrenheit
        round_result (bool, optional): Whether or not to round the result. Defaults to True.

    Returns:
        float: The temperature in celsius
    """
    return round((fahrenheit - 32) * 5/9) if round else (fahrenheit - 32) * 5/9
    
def describe_weather_code(weathercode: int):
    """This uses the weathercodes.py file to get a description of the weather code

    Args:
        weathercode (int): The weathercode to fetch the description of

    Returns:
        str: The description of the weather code
    """
    if isinstance(weathercode, int):
        if len(str(weathercode)) == 1:
            weathercode = f"0{weathercode}"
    return CODES[str(weathercode)]

# https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
def weather_code_to_image(weathercode: int):
    """Converts a weather code to an image path, if the weather code is not found, it returns a default image

    Args:
        weathercode (int): The weather code to get the image for

    Returns:
        str: the path to the weather image, which is just a gif of an emoji
    """
    if weathercode < 20:
        if weathercode in {11, 12}:
            return "assets/rain.gif"
        return "assets/fog.gif" if weathercode == 5 else "assets/clear.gif"
    elif weathercode < 30:
        if weathercode in {22, 23, 24}:
            return "assets/snow.gif"
        elif weathercode == 28:
            return "aassets/fog.gif"
        elif weathercode == 29:
            return "assets/storm.gif"
        else:
            return "assets/rain.gif"

    elif weathercode < 50:
        return "assets/fog.gif"

    elif weathercode < 70:  # drizzle
        return "assets/rain.gif"

    elif weathercode < 80:
        return "assets/snow.gif"

    elif weathercode < 85:
        return "assets/rain.gif"

    elif weathercode < 91:
        return "assets/snow.gif"

    elif weathercode < 100:
        return "assets/rain.gif"
            

    return f"assets/{weathercode}.gif"

def angle_to_cardinal(angle: int) -> str:  # N, NE, E, SE, S, SW, W, NW
    # Credit https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f
    cardinalDirections = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return cardinalDirections[round(angle / 45) % 8]