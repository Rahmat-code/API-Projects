import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

account_sid = os.getenv('account_sid')
if not account_sid:
    raise ValueError("Twilio account SID not found in environment variables.")
auth_token = os.getenv('auth_token')
if not auth_token:
    raise ValueError("Twilio auth token not found in environment variables.")   

api_key = "652b4a71fb61e625177288af78e4f8ef"
MY_LAT = 22.572645  # Your latitude
MY_LONG = 88.363892 # Your longitude

def get_weather():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "cnt": 4,
        "appid": api_key,
    }
    print("Fetching weather data...")
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    return response.json()

will_rain_today = False

def rain_alerrt(weather_data):
    for forcast in weather_data["list"]:
        weather_id = forcast["weather"][0]["id"]
        if int(weather_id) < 700:
            will_rain_today = True
    return will_rain_today


weather_data = get_weather()
#print(weather_data)
will_rain_today = rain_alerrt(weather_data)
print(f"Will it rain today? {will_rain_today}")

if will_rain_today:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid= 'HX229f5a04fd0510ce1b071852155d3e75',
    content_variables='{"1":"It will rain today. Carry an umbrella.☂️"}',   
    to='whatsapp:+917980498648'
    )

    print(message.status)