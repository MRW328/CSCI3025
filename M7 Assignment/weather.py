#Matthew Williams
#CSCI3025

import requests
#this program takes a user input for a city, gets the coordinates of that city from an api, and uses 
#those coordinates to pull weather data from another api

#getCoordinates function will fetch the coordinates of a user input city 
def getCoordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    #these parameters tell the API whaat we're looking for
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    #sends the get request to the API using the parameters above. 10 second forced time out 
    response = requests.get(url, params=params, timeout=10)

    #raises an error based on status code
    response.raise_for_status()

    #JSON to python conversion 
    data = response.json()

    #data validation
    if "results" not in data or len(data["results"]) == 0:
        raise ValueError(f"City '{city}' not found. Try a different spelling.")

    #return values 
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"], result["country"]


#using latitude and ongitude value from previous function, we call the weather API to get the weather
def getWeather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    #request specific current weather fields from the api
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    #json to python dictionary
    return response.json()


#Since the weather api returns weather codes, we define them here
def description(code):
    
    codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Icy fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Light showers",
        81: "Moderate showers",
        82: "Heavy showers",
        95: "Thunderstorm",
    }
    #returns definition for corresponding code or "Unknown conditions" if the code isnt defined above
    return codes.get(code, "Unknown conditions")


#main
def main():
    #user inputs city name
    city = input("Enter a city name: ").strip()

    try:
        
        print(f"\nLooking up coordinates for '{city}'...")
        #getCoordingates function returns values for latitude, longitude city and country
        lat, lon, city, country = getCoordinates(city)

        print(f"Found: {city}, {country} ({lat}, {lon})")
        print("Fetching current weather...\n")

        #get the current weather data 
        weatherData = getWeather(lat, lon)
        current = weatherData["current"]

        #extract the individual values from the dictionary
        temp = current["temperature_2m"]
        wind = current["wind_speed_10m"]
        humidity = current["relative_humidity_2m"]
        condition = description(current["weather_code"])

        #print the results in a readable format
        print(f"Current Weather for {city}, {country}")
        print("-" * 40)
        print(f"Condition:    {condition}")
        print(f"Temperature:  {temp}°F")
        print(f"Humidity:     {humidity}%")
        print(f"Wind Speed:   {wind} mph")
        print("-" * 40)

    #error handling
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again in a moment.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error — {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Unexpected data format. Missing field: {e}")


if __name__ == "__main__":
    main()