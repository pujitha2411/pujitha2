import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {
    'latitude': 40.71,
    'longitude': -74.01,
    'current_weather': True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    current_weather = data.get("current_weather", {})
    if current_weather:
        print("Temperature:", current_weather["temperature"], "°C")
        print("Wind Speed:", current_weather["windspeed"], "km/h")
        print("Weather Code:", current_weather["weathercode"])
    else:
        print("No current weather data found.")
else:
    print("API request failed with status code:", response.status_code)
