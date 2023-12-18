import tkinter as tk
from . import naming
from . import weatherfetch
from . import utils
from . import _meta

class GUI(tk.Tk):

    def refresh(self):
        """Refreshes the GUI and redraws all ui elements except the input box and buttons
        """
        if not self.inputBox.get().replace(" ", ""):
            self.alert("Please enter a city name")
            return

        try:
            city_name = self.inputBox.get()
            naming.get_coordinates(city_name)
            weather = weatherfetch.get_weather(naming.get_coordinates(city_name))
        except Exception as e:
            self.alert(f"Error: {e}")
            return

        temp_str = f"{utils.celsius_to_fahrenheit(weather['temperature_2m'])}°F ({weather['temperature_2m']}°C)" \
                if  not _meta.CELSIUS_MODE else f"{weather['temperature_2m']}°C ({utils.celsius_to_fahrenheit(weather['temperature_2m'])}°F)"
    
        self.tempLabel.pack_forget()
        self.tempLabel.config(text=f"Temperature: {temp_str}")
        self.tempLabel.pack(fill="x")


        feels_like_str = f"{utils.celsius_to_fahrenheit(weather['apparent_temperature'])}°F ({weather['apparent_temperature']}°C)" \
                            if not _meta.CELSIUS_MODE else f"{weather['apparent_temperature']}°C ({utils.celsius_to_fahrenheit(weather['apparent_temperature'])}°F)"
    
        self.feelsLikeLabel.pack_forget()
        self.feelsLikeLabel.config(text=f"Feels Like: {feels_like_str}")
        self.feelsLikeLabel.pack(fill="x")

        self.humidityLabel.pack_forget()
        self.humidityLabel.config(text=f"Humidity: {weather['relative_humidity_2m']}%")
        self.humidityLabel.pack(fill="x")

        self.windSpeedLabel.pack_forget()
        self.windSpeedLabel.config(text=f"Wind Speed: {weather['wind_speed_10m']}m/s")
        self.windSpeedLabel.pack(fill="x")

        self.windGustsLabel.pack_forget()
        self.windGustsLabel.config(text=f"Wind Gusts: {weather['wind_gusts_10m']}m/s")
        self.windGustsLabel.pack(fill="x")

        self.windDirectionLabel.pack_forget()
        self.windDirectionLabel.config(text=f"Wind Direction: {utils.angle_to_cardinal(weather['wind_direction_10m'])} ({weather['wind_direction_10m']}°)")
        self.windDirectionLabel.pack(fill="x")

        self.precipitationLabel.pack_forget()
        self.precipitationLabel.config(text=f"Precipitation: {weather['precipitation']}mm")
        self.precipitationLabel.pack(fill="x")  

        self.imageLabel.pack_forget()
        path = utils.weather_code_to_image(weather["weather_code"])
        img = tk.PhotoImage(file=path, master=self)
        self.imageLabel.config(image=img)
        self.imageLabel.image = img
        self.imageLabel.pack(fill="x")

        self.weatherForecast.pack_forget()
        self.weatherForecast.config(wraplength=600)
        self.weatherForecast.config(justify="center")
        self.weatherForecast.config(text=utils.describe_weather_code(weather["weather_code"]))
        self.weatherForecast.pack(fill="x", )

    def toggleCF(self):
        # toggles celsius mode and refreshes the gui
        _meta.CELSIUS_MODE = not _meta.CELSIUS_MODE
        self.refresh()     

    def alert(self, text, title:str = "Alert"):
        """Create an alert popup to display an error or message

        Args:
            text (str): The text to display in the alert
            title (str, optional): The title of the alert. Defaults to "Alert".
        """

        alert = tk.Toplevel(self)
        alert.title(title)
        alert.geometry("300x100")
        alert.resizable(False, False)

        alertLabel = tk.Label(alert, text=text, font=("Arial", 14))
        alertLabel.config(wraplength=250)
        alertLabel.pack()

        alertButton = tk.Button(alert, text="OK", command=alert.destroy)
        alertButton.pack()

        alert.mainloop()



    def __init__(self):
        super().__init__()
        self.title("Weather")
        self.geometry("700x700")

        # draw the intial ui elements
        self.weatherLabel = tk.Label(self, text="WeatherGuy", font=("Times New Roman", 20))
        self.weatherLabel.pack()

        self.hintLabel = tk.Label(self, text="Enter a city name to get the weather", font=("Arial", 14))
        self.hintLabel.pack()

        self.inputBox = tk.Entry(self)
        self.inputBox.pack()
    
        # draw the buttons
        self.submitButton = tk.Button(self, text="Get Weather", command=self.refresh)
        self.submitButton.pack()
        self.toggleCFButton = tk.Button(self, text="Toggle C/F", command=self.toggleCF)
        self.toggleCFButton.pack()
        self.exitButton = tk.Button(self, text="Exit", command=self.destroy)
        self.exitButton.pack()


        # create all the ui elements but don't actually pack (draw) them yet
        self.weatherForecast = tk.Label(self, text="Weather", font=("Arial", 14), justify="left")
        self.tempLabel = tk.Label(self, text="Temperature", font=("Arial", 14), justify="left")
        self.feelsLikeLabel = tk.Label(self, text="Feels Like", font=("Arial", 14), justify="left")
        self.humidityLabel = tk.Label(self, text="Humidity", font=("Arial", 14), justify="left")
        self.windSpeedLabel = tk.Label(self, text="Wind Speed", font=("Arial", 14), justify="left")
        self.windGustsLabel = tk.Label(self, text="Wind Gusts", font=("Arial", 14), justify="left")
        self.windDirectionLabel = tk.Label(self, text="Wind Direction", font=("Arial", 14), justify="left")
        self.precipitationLabel = tk.Label(self, text="Precipitation", font=("Arial", 14), justify="left")
        self.imageLabel = tk.Label(self)

        self.resizable(False, False)
        self.mainloop()

def gui():
    GUI()