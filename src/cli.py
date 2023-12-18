import sys
from .naming import *
from .weatherfetch import *
from .utils import *
from ._meta import *
import datetime

def get_temp_color(temp):

    red_hot_threshold = 90 if CELSIUS_MODE else 32
    green_warm_threshold = 70 if CELSIUS_MODE else 21

    if temp >= red_hot_threshold:
        return colors.red
    elif temp >= green_warm_threshold:
        return colors.green
    else:
        return colors.blue
    
def get_humidity_color(humidity):
    if humidity >= 80:
        return colors.blue
    elif humidity >= 60:
        return colors.green
    elif humidity >= 40:
        return colors.yellow
    else:
        return colors.red
    
def get_target_city():
    # combs through sys.argv for a city name, allows spaces in city names
    # returns the city name or None if not found
    city_name = ""
    for arg in sys.argv:
        if arg.startswith("-") or arg == sys.argv[0]:
            continue
        else:
            city_name += arg + " "
    city_name = city_name.strip()
    if city_name == "":
        return None
    else:
        return city_name

def cli():
    cprint(f"WeatherGuy v{VERSION_NUMBER}", colors.bold)
    city_name = get_target_city()
    print(f"Fetching weather for {colors.bold}{city_name}{colors.end}...")
    try:
        coords = get_coordinates(city_name)
    except ValueError:
        print(f"City name {city_name} not found")
        exit(1)
    except urllib.error.URLError:
        print(f"HTTP or internet error")
        exit(1)
    
    try:
        weather = get_weather(coords)
    except ValueError:
        print(f"Coordinates {coords} not found")
        exit(1)
    except urllib.error.URLError:
        print(f"HTTP or internet error")
        exit(1)

    today_str = "Today" if weather['is_day'] else "Tonight"
    # '2023-12-07T03:15'
    date_str = datetime.datetime.strptime(weather['time'], "%Y-%m-%dT%H:%M").strftime("%A, %B %d, %Y")

    # l pipe symbol: \u2502 
    print(f"Weather for {colors.bold}{city_name}{colors.end}")
    print(f"╠╡ {today_str} ({date_str})")
    print(f"╠╡ {describe_weather_code(weather['weather_code'])}")

    
    temp_str = f"{celsius_to_fahrenheit(weather['temperature_2m'])}°F ({weather['temperature_2m']}°C)" \
                if  not CELSIUS_MODE else f"{weather['temperature_2m']}°C ({celsius_to_fahrenheit(weather['temperature_2m'])}°F)"

    temp_color = get_temp_color(weather['temperature_2m'])

    print(f"╠═╡ Temperature:       {temp_color}{colors.bold}{temp_str}{colors.end}")

    feels_like_str = f"{celsius_to_fahrenheit(weather['apparent_temperature'])}°F ({weather['apparent_temperature']}°C)" \
                        if not CELSIUS_MODE else f"{weather['apparent_temperature']}°C ({celsius_to_fahrenheit(weather['apparent_temperature'])}°F)"

    print(f"╠═╡ Feels Like:        {temp_color}{colors.bold}{feels_like_str}{colors.end}")

    print(f"╠═╡ Relative Humidity: {get_humidity_color(weather['relative_humidity_2m'])}{colors.bold}{weather['relative_humidity_2m']}%{colors.end}")

    print(f"╠═╡ Wind Speed:        {colors.bold}{weather['wind_speed_10m']}mph{colors.end}")

    print(f"╠═╡ Wind Gusts:        {colors.bold}{weather['wind_gusts_10m']}mph{colors.end}")

    print(f"╠═╡ Wind Direction:    {colors.bold}{angle_to_cardinal(weather['wind_direction_10m'])} ({weather['wind_direction_10m']}°){colors.end}")

    found_precipitation = False

    if weather['rain'] > 0:
        print(f"╠═╡ Rain:              {colors.bold}{weather['rain']}mm{colors.end}")
    
    if weather['snowfall'] > 0:
        print(f"╠═╡ Snowfall:          {colors.bold}{weather['snowfall']}mm{colors.end}")
    
    if weather['precipitation'] > 0 and weather['precipitation'] >= weather['rain'] + weather['snowfall']:
        print(f"╠═╡ Precipitation:     {colors.bold}{weather['precipitation']}mm{colors.end}")
    
    print(f"╚══ Weather Code:      {colors.bold}{weather['weather_code']}{colors.end}")