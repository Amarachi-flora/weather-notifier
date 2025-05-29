# 🌤️ Weather Notifier

A real-time weather app built with Python and Streamlit that fetches and displays current weather data for any city using the OpenWeatherMap API.

---

##  What It Does

- Prompts the user to enter a city name.
- Fetches weather data via the OpenWeatherMap API.
- Displays:
  - Temperature (°C)
  - Weather condition (e.g., Clear, Rain, Clouds)
  - Humidity
  - Wind Speed
- Shows smart alerts:
  - “It’s quite hot in Lagos today!”
  - “It’s chilly in Nairobi, dress warm!”
  - “The weather in Accra seems pleasant.”

---

## Technologies Used

- Python
- [Streamlit](https://streamlit.io/)
- [Requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

##  Project Structure

weather-notifier/
├── weather_notifier.py # Main Streamlit app
├── .env # Environment variables (your API key)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Setup Instructions

1. **Clone this repo:** 


```bash
- git clone https://github.com/your-username/weather-notifier.git
- cd weather-notifier

 

# Create and activate a virtual environment

- python -m venv venv

# Windows
- .\venv\Scripts\activate

# macOS/Linux
- source venv/bin/activate



#Install dependencies
- pip install -r requirements.txt



#Create a .env file and add your OpenWeatherMap API key
- Create a .env file and add your OpenWeatherMap API key


# run the app 
- streamlit run weather_notifier.py
