#Matthew Williams
#CSCI3025
#ive been using camel case this semester and have adopted snake_case for this project

import requests
from location import Location
from forecast import Forecast
import os

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    #these parameters tell the API what we're looking for
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

    #return location object
    return Location(
        result["name"], 
        result["country"], 
        result["latitude"], 
        result["longitude"],
        admin1 = result.get("admin1"),
        )

def get_forecast(latitude, longitude, days=7):
    """Fetch a daily forecast from Open-Meteo for the given coordinates.
       Returns the parsed JSON response as a dictionary"""
      
    params = {

        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max",
        "timezone": "auto",
        "forecast_days": days,
        "temperature_unit": "fahrenheit",
    }
    
    url = "https://api.open-meteo.com/v1/forecast"
   
    response = requests.get(url, params=params)
  
    return response.json()


if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    
    try:
        loc = get_coordinates(city)
        data = get_forecast(loc.latitude, loc.longitude)
        forecast = Forecast(loc, data)
        print(forecast)
        forecast.print_table()
        forecast.summary()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, "forecast.png")
        forecast.plot(output_path)
        

    except ValueError as e:
        print(f"Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error — {e}") 
    