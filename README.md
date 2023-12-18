# WeatherGuy
## Type in a city, get the weather

```
> python main.py  -?   
 
Usage: python3 main.py [options] [optional: city name]
 Testing:
  --test:         Run the entire test suite
  --testnom:      Run the test suite without mocking
  --testweather:  Run the weather test suite
  --getcoords:    Get the coordinates of a city, then exit.
 Options:
  --gui:          Run the GUI
  --cli:          Run the CLI (ex. python3 main.py --cli New York City)
  --celsius, -c:  Use celsius instead of fahrenheit
  --help, -h, -?: Display this help message
```

# Usage

## GUI (default)
`python main.py`

## CLI (fancier, more polished at the moment)
`python main.py --cli [city name]`

ex. `python main.py --cli Valparaiso, IN`

## Testing
`python main.py --test`

Tests both the naming and weather fetching code, then runs the gui

# TODO
 - [ ] Error Window
 - [ ] Exit Button