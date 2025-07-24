### WEATHER APP ###

# Command-line application that takes user input of a city name and displays the current weather for that city.
#API is weatherapi.com
from dotenv import load_dotenv

class WeatherService():
    def __init__(self, api_key):
        self.api_key = api_key
