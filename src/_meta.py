import sys

# This is the version number
VERSION_NUMBER = "1.0"

# This was required for the weather API I used from the NWS, but not for
# openmeteo.org. Still keeping this here in case I need it later.
CONTACT_EMAIL = "rmcguire40@ivytech.edu"

# this is whether or not to display the temperature in celsius or fahrenheit
# it is set initially with the -c or --celsius command line arguments
# but can also be toggled with the button in the GUI
CELSIUS_MODE = "--celsius" in sys.argv or "-c" in sys.argv

# A dictionary of city names and their coordinates, used for testing name to coordinates conversion
TEST_CITIES = {
        "Chicago": (41.8755616, -87.6244212),
        "London": (51.5074456, -0.1277653),
        "Paris": (48.8588897, 2.3200410217200766),
        "NYC": (40.7127281, -74.0060152),
        "Tokyo": (35.6821936, 139.762221),
        "Cairo": (37.0057958, -89.1772449),
        "Valparaiso, IN": (41.4730948, -87.0611412),
        "Chesterton, USA": (41.6105938, -87.0641992),
        "Michigan City": (41.7075394, -86.8950297)
}
