from src.gui import *
from src.cli import *
from src.naming import *
from src.utils import *
from src.weatherfetch import *
import sys

if "--help" in sys.argv or "-h" in sys.argv or "-?" in sys.argv:
    # so i don't have to change this if i rename the file
    filename = sys.argv[0]

    print(f"Usage: python3 {filename} [options] [optional: city name]")
    print(" Testing:")
    print("  --test:         Run the entire test suite")
    print("  --testnom:      Run the test suite without mocking")
    print("  --testweather:  Run the weather test suite")
    print("  --getcoords:    Get the coordinates of a city, then exit.")
    print(" Options: ")
    print("  --gui:          Run the GUI")
    print(f"  --cli:          Run the CLI (ex. python3 {filename} --cli New York City)")
    print("  --celsius, -c:  Use celsius instead of fahrenheit")
    print("  --help, -h, -?: Display this help message")
    print("")
    exit(0)

if "--test" in sys.argv or "--testnom" in sys.argv:
    get_coordinates_test()

if "--test" in sys.argv or "--testweather" in sys.argv:
    get_weather_test()

if "--getcoords" in sys.argv:
    city_name = get_target_city()
    print(f"\"{city_name}\": {get_coordinates(city_name)}")
    exit(0)

# main routine
 
if "--cli" in sys.argv and get_target_city() is not None:
    cli()
else:
    gui()
