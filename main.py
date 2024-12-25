import requests

# API endpoints
weather_url = "https://api.openweathermap.org/data/2.5/weather"
sun_url = "https://api.sunrisesunset.io/json"
time_url = "https://worldtimeapi.org/api/timezone/America/Toronto"

# API parameters
lat, lon = 43.551915, -79.579578
weather_api_key = "801470731a163b794712c34ea5fd3a56" 

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
cur_hour = int(cur_time[:2])
cur_minute = int(cur_time[3:5])

cur_total = cur_hour*60 + cur_minute

# Extract weather details
temp = str(round(int(weather_info["main"]["temp"])))
weather_type = weather_info["weather"][0]["main"]
weather_description = weather_info["weather"][0]["description"]

# Extract and adjust sunrise and sunset times
twelve = str(int(sun_info["results"]["sunset"][0]) + 12)
sunset_time = twelve + sun_info["results"]["sunset"][1:7]
sunrise_time = sun_info["results"]["sunrise"][:7]

if len(sunset_time) == 7:
    sunset_time = "0" + sunset_time
if len(sunrise_time) == 7:
    sunrise_time = "0" + sunrise_time

set_hour = int(sunset_time[:2])
set_minute = int(sunset_time[3:5])
rise_hour = int(sunrise_time[:2])
rise_minute = int(sunrise_time[3:5])

set_total = set_hour*60 + set_minute
rise_total = rise_hour*60 + rise_minute

# Determine weather intensity
if "light" in weather_description:
    intensity = 0
elif "heavy" in weather_description or "extreme" in weather_description:
    intensity = 2
else:
    intensity = 1

# Determine sun position
if cur_total < rise_total:
    sun_degree = -1  
elif cur_total > set_total:
    sun_degree = -1  
else:
    sun_degree = 180 - (((cur_total - rise_total) / (set_total - rise_total)) * 180)

# Generate full description
full_description = cur_time + ". Home: "
if weather_type == "Clouds":
    full_description += f"It is {temp} degrees Celsius. There are {weather_description}."
elif weather_type == "Snow":
    full_description += f"It is {temp} degrees Celsius. There is {weather_description}."
else:
    full_description += f"It is {temp} degrees Celsius. There is a {weather_description}."


print(full_description)

"""
weather intensity - 0,1,2
weather type - rain, clouds, sun, snow etc
sun angle set - 0-180 or -1 if sun has not risen or has fallen
"""
