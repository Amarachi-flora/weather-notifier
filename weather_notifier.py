import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Set page config (optional, but looks nicer)
st.set_page_config(page_title="Weather Notifier", page_icon="🌤️", layout="centered")

# App title and description
st.title("🌤️ Real-Time Weather Notifier")
st.subheader("Check the current weather of any city")

# User input: city name
city = st.text_input("Enter City Name")

def get_weather(city_name):
    """Fetch weather data from OpenWeatherMap API."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {e}")
        return None

if st.button("Get Weather"):
    if city.strip():
        data = get_weather(city.strip())

        if data:
            temp = data['main']['temp']
            condition = data['weather'][0]['main']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Display weather info
            st.success(f"Temperature: {temp}°C")
            st.info(f"Condition: {condition}")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Wind Speed: {wind_speed} m/s")

            # Smart alerts based on temperature
            if temp > 30:
                st.warning(f" It's quite hot in {city.title()} today. Stay hydrated!")
            elif temp < 18:
                st.warning(f" It's chilly in {city.title()}, dress warm!")
            else:
                st.success(f" The weather in {city.title()} seems pleasant.")
        else:
            st.error("Could not retrieve weather data. Check the city name or try again later.")
    else:
        st.error("Please enter a city name.")
