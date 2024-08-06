import requests

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city, units='metric'):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def display_weather(data, units):
    if data:
        city = data.get('name')
        weather = data.get('weather')[0].get('description').capitalize()
        temperature = data.get('main').get('temp')
        humidity = data.get('main').get('humidity')

        unit_symbol = 'C' if units == 'metric' else 'F'
        
        print(f"\nWeather in {city}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}°{unit_symbol}")
        print(f"Humidity: {humidity}%")
    else:
        print("Failed to retrieve data.")

def main():
    print("Weather Information CLI Tool")
    print("---------------------------")

    city = input("Enter city name: ")
    unit_choice = input("Choose temperature unit: (1) Celsius (2) Fahrenheit: ")

    units = 'metric' if unit_choice == '1' else 'imperial'

    data = get_weather(city, units)
    display_weather(data, units)

if __name__ == '__main__':
    main()
