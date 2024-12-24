import requests

# API endpoints
weather_url = "https://api.openweathermap.org/data/2.5/weather"
sun_url = "https://api.sunrisesunset.io/json"
time_url = "https://worldtimeapi.org/api/timezone/America/Toronto"

# API parameters
lat, lon = 43.551915, -79.579578
weather_api_key = "Weather_API_Key"

# Fetch data from APIs
weather_response = requests.get(
    f"{weather_url}?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
)
sun_response = requests.get(f"{sun_url}?lat={lat}&lng={lon}")
time_response = requests.get(time_url)

# Parse JSON responses
time_info = time_response.json()
weather_info = weather_response.json()
sun_info = sun_response.json()

# Extract current time
cur_time = time_info["datetime"][11:16]

# Extract weather details
temp = str(round(int(weather_info["main"]["temp"])))
weather_type = weather_info["weather"][0]["main"]
weather_description = weather_info["weather"][0]["description"]

# Extract and adjust sunrise and sunset times
twelve = str(int(sun_info["results"]["sunset"][0]) + 12)
sunset = twelve + sun_info["results"]["sunset"][1:7]
sunrise = sun_info["results"]["sunrise"][:7]

# Determine weather intensity
if "light" in weather_description:
    intensity = 0
elif "heavy" in weather_description or "extreme" in weather_description:
    intensity = 2
else:
    intensity = 1

full_description = "Home: "
# Generate full description
if weather_type == "Clouds":
    full_description += f"It is {temp} degrees Celsius. There are {weather_description}."
elif weather_type == "Snow":
    full_description += f"It is {temp} degrees Celsius. There is {weather_description}."
else:
    full_description += f"It is {temp} degrees Celsius. There is a {weather_description}."


print(full_description)

"""

"""
