import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='')

@app.route("/get_weather", methods=["GET"])
def get_weather():
    api_key = "e061673116b23f148c7119f3bbd9cf34"
    location = request.args.get("location")
    weather_data = get_weather_data(api_key, location)
    if "current" in weather_data:
        weather = parse_weather_data(weather_data)
        return jsonify(weather)
    else:
        return jsonify({"error": "Error retrieving weather data. Please try again."}), 400

@app.route("/")
def index():
    return render_template("main.html")

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

if __name__ == "__main__":
    app.run()
