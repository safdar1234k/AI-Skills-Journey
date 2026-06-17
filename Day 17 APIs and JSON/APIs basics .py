import requests
from datetime import datetime
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=31.15&longitude=70.95&current_weather=true")
data = response.json()
print(data)
temperature = data['current_weather']['temperature']
wind_speed = data['current_weather']['windspeed']
time_now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

with open("weather_dat.txt", "a", encoding="utf-8") as file:
    file.write(f"Temperature: {temperature}°C, Wind Speed: {wind_speed} km/h, Time: {time_now}\n")
    print("weather data has been loaded")
print(f"current temperature: {temperature}°C")
print(f"current wind speed : {wind_speed} km/h")
print(f"Time: {time_now}")