import requests
from datetime import datetime


def get_current_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # we can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nCurrent weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")


def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/onecall"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather forecast for the next 7 days in {city}:")
            for day in data['daily']:
                date = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
                print(f"\n{date}:")
                print(f"   Temperature: Day - {day['temp']['day']}°C, Night - {day['temp']['night']}°C")
                print(f"   Description: {day['weather'][0]['description']}")
                print(f"   Humidity: {day['humidity']}%")
                print(f"   Wind Speed: {day['wind_speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    api_key = 'a5e5727ba6935990b0e8c8ecb893f53a'
    city = input("Enter the city name: ")

    get_current_weather(api_key, city)
    get_weather_forecast(api_key, city)
