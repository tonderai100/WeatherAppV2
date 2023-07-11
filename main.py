import requests
import json

def get_weather_data(api_key, location):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    response = requests.get(url)
    data = response.json()
    return data

def parse_weather_data(data):
    weather = {
        "temperature": data["current"]["temperature"],
        "humidity": data["current"]["humidity"],
        "wind_speed": data["current"]["wind_speed"],
        "conditions": data["current"]["weather_descriptions"][0]
    }
    return weather

def display_weather(weather):
    print("Current Weather Conditions:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} km/h")
    print(f"Conditions: {weather['conditions']}")

def main():
    api_key = "e061673116b23f148c7119f3bbd9cf34"
    location = input("Enter location: ")
    weather_data = get_weather_data(api_key, location)
    if "current" in weather_data:
        weather = parse_weather_data(weather_data)
        display_weather(weather)
    else:
        print("Error retrieving weather data. Please try again.")

if __name__ == "__main__":
    main()
