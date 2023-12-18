import urllib.request
import urllib.parse
import json
from typing import TypedDict, Tuple

from .utils import cprint, colors
from . import _meta

def get_weather_test():
    """Run a test on the subsystem that fetches weather data.
    """
    keys = _meta.TEST_CITIES

    requiredResponseKeys = ['time', 'interval', 'temperature_2m', 'relative_humidity_2m', 'apparent_temperature', 'is_day', 'precipitation', 'rain', 'showers', 'snowfall', 'weather_code', 'cloud_cover', 'pressure_msl', 'surface_pressure', 'wind_speed_10m', 'wind_direction_10m', 'wind_gusts_10m']

    cprint("Running get_weather_test", colors.bold)

    for key in keys:
        try:
            weather = get_weather(keys[key])
            assert all(key in weather for key in requiredResponseKeys)
            cprint(f"Test passed for {key}", colors.green)
        except Exception as e:
            exception_desc = str(e)
            cprint(f"Test failed for {key}", colors.red)
            if isinstance(e, ValueError):
                cprint(f"This is likely because the coordinates were not found ({exception_desc})", colors.yellow)
            elif isinstance(e, urllib.error.URLError):
                cprint(f"This is likely because there was an http or internet error ({exception_desc})", colors.yellow)
            elif isinstance(e, AssertionError):
                cprint(f"Expected ({requiredResponseKeys}) - Got ({weather.keys()}) ({exception_desc})", colors.yellow)
            else:
                cprint(f"Unknown error ({exception_desc})", colors.yellow)

    cprint("Finished get_weather_test", colors.bold)

class weatherResponse(TypedDict):
    """this is the response from the open-meteo.com api, TypedDict gives us type hints for the response, so we 
    Don't have to guess what the response looks like or memorize the keys
    """
    time: str
    interval: int
    temperature_2m: float
    relative_humidity_2m: int
    apparent_temperature: float
    is_day: int
    precipitation: float
    rain: float
    showers: float
    snowfall: float
    weather_code: int
    cloud_cover: int
    pressure_msl: float
    surface_pressure: float
    wind_speed_10m: float
    wind_direction_10m: int
    wind_gusts_10m: float


def get_weather(coords: tuple) -> weatherResponse:
    """Get the weather for a set of coordinates

    Args:
        coords (tuple): The coordinates of the location to get the weather for

    Returns:
        weatherResponse: a dictionary of weather data
    """

    # unpack the coordinates tuple to make them easier to work with
    lat = coords[0]
    lon = coords[1]

    # the url to send the web request to
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m"

    # actually make the request
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # decode the response from the api into a dictionary
        data = json.loads(response.read().decode())

        return data["current"]