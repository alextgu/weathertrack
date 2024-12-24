Weather Animation Project

This project includes both the backend and frontend for a weather-based animation system. The backend fetches live weather data, sunrise and sunset times, and the current time to determine animations based on weather conditions. The frontend uses HTML, CSS, and JavaScript to display dynamic animations based on the backend data.

Features

Backend fetches weather data from OpenWeatherMap.

Retrieves sunrise and sunset times from the Sunrise Sunset API.

Gets local time using WorldTimeAPI.

Analyzes weather conditions to determine intensity and type.

Frontend dynamically updates animations based on backend data.

Try it yourself:

**Prerequisites**

Python 3.7 or later

An OpenWeatherMap API key

**Installation**

Clone the repository:

git clone https://github.com/your-username/weather-animation-project.git
cd weather-animation-project

Install dependencies for the backend:

pip install requests python-dotenv

Create a .env file for your API key:

WEATHER_API_KEY = your_openweathermap_api_key
[https://docs.openweather.co.uk/faq#:~:text=Is%20OpenWeather%20API%20free%3F,60%20free%20calls%20per%20minute.](https://docs.openweather.co.uk/)

Add .env to .gitignore to keep it private:

# .gitignore
.env

Usage

Backend

Run the script to fetch weather data:

python main.py

**License**

This project is licensed under the MIT License.

**Acknowledgments**

OpenWeatherMap API

Sunrise Sunset API

WorldTimeAPI
