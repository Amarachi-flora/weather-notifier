# 🌤️ Weather Notifier

A real-time weather app built with Python and Streamlit that fetches and displays current weather data for any city   
using the OpenWeatherMap API.

## Problem & Solution

## The Problem

Millions of people around the world face challenges due to unpredictable weather and limited access to accurate, real-time forecasts. Whether it's planning a commute, a trip, or just choosing what to wear, not knowing the current weather can lead to discomfort, poor decisions, or even safety risks. In many developing regions, access to modern weather services is minimal or non-existent.

##  The Solution

Weather Notifier is a simple, real-time weather app that helps users check current conditions in any city instantly. It:

- Fetches live weather updates via the OpenWeatherMap API

- Displays essential metrics like temperature, weather conditions, humidity, and wind speed

- Provides smart, user-friendly alerts to help users prepare for the day

By offering a fast, accessible interface built with Python and Streamlit, the app empowers users—regardless of location or device—to make weather-smart decisions and reduce everyday risks tied to weather uncertainty.

## What It Does

1. Prompts the user to enter a city name.

2. Fetches weather data via the OpenWeatherMap API.

## Displays:

- Temperature (°C)

- Weather condition (e.g., Clear, Rain, Clouds)

- Humidity

- Wind Speed

## Shows smart alerts:

-  “It’s quite hot in Lagos today!”

- “It’s chilly in Nairobi, dress warm!”

- “The weather in Accra seems pleasant.”

## Technologies Used

1. Python

2. Streamlit

3. Requests

4. python-dotenv

5. OpenWeatherMap API

## Project Structure

weather-notifier/
├── weather_notifier.py       # Main Streamlit app  
├── .env                      # Environment variables (your API key)  
├── requirements.txt          # Python dependencies  
└── README.md                 # Project documentation

## Setup Instructions

Clone this repo:

git clone https://github.com/your-username/weather-notifier.git
cd weather-notifier

#  Create and activate a virtual environment:

# Create virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt

# Create a .env file and add your OpenWeatherMap API key:
API_KEY=your_openweathermap_api_key_here

# Run the app:
streamlit run weather_notifier.py


---

## Live Demo

Try the Weather Notifier app online here:  
- [https://weather-notifier.streamlit.app/](https://weather-notifier.streamlit.app/)  


Get real-time weather updates for any city, anytime.
