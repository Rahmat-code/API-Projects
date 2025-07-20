import requests
from datetime import datetime

def get_sunrise_sunset(latitude, longitude):
    url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    if response.status_code == 200:
        data = response.json()
        sunrise = data['results']['sunrise']
        sunset = data['results']['sunset']
        #print(f"Sunrise: {sunrise}, Sunset: {sunset}")
        
        # Convert to datetime objects
        sunrise_time = datetime.fromisoformat(sunrise.replace('Z', '+00:00'))
        sunset_time = datetime.fromisoformat(sunset.replace('Z', '+00:00'))
        
        return sunrise_time, sunset_time
    else:
        raise Exception("Error fetching data from the API")
    
def main():
    latitude = 40.7128  # Example: New York City
    longitude = -74.0060
    
    try:
        sunrise, sunset = get_sunrise_sunset(latitude, longitude)
        print(f"Sunrise: {sunrise.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Sunset: {sunset.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"An error occurred: {e}")    

main()  # Call the main function to execute the code    