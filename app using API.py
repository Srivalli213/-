import requests

def get_weather(city, api_key):
    """
    Fetch weather data from OpenWeatherMap API for the given city.
    """
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract and format weather details
        weather_desc = data['weather'][0]['description'].title()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city.title()}:")
        print(f"Condition : {weather_desc}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity   : {humidity}%")
        print(f"Wind Speed : {wind_speed} m/s\n")

    except requests.exceptions.HTTPError:
        print("City not found. Please check the spelling.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except KeyError:
        print("Unexpected data format from the API.")

if __name__ == "__main__":
    # Replace with your own API key from OpenWeatherMap
    API_KEY = "YOUR_API_KEY_HERE"
    city_name = input("Enter city name: ").strip()
    get_weather(city_name, API_KEY)
