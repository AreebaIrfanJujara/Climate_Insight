import requests
def get_coordinates(name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    extra = {
        "name": name,
        "count": 1
    }

    try:
        response = requests.get(url, params=extra)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
        print("network error:", e)
        return None

    print("API Response:", data)

    if "results" in data:
        return data["results"][0]["latitude"], data["results"][0]["longitude"]

    else:
        print(f"No results found for {name}")
        return None
    





def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    info = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }

    try:
        response = requests.get(url, params=info, timeout=10)
        response.raise_for_status()

        data = response.json()

    except requests.RequestException as e:
        print("Network error:", e)
        return None

    print("weather API responded with:", data)

    if "current" in data:
        weather = data["current"]["temperature_2m"]
        unit = data["current_units"]["temperature_2m"]

        print(f"Current weather is {weather} {unit}")
        return weather, unit

    else:
        print("NO current weather data is found")
        return None


coordinates=get_coordinates("Karachi")
              
if coordinates:
    lat,lon=coordinates
    print(f"Fetching data for {lat},{lon}")
    get_weather(lat,lon)
else:
    print("Could not fetch coordinates for the given location.")    


def get_climate_history(lat, lon):
    
    endpoint = "https://archive-api.open-meteo.com/v1/archive"


    info = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "1980-01-01",
        "end_date": "2025-12-31",
        "daily": "temperature_2m_mean",
        "timezone": "auto",
    }
    try:
        response = requests.get(endpoint, params=info, timeout=10).json()
        temps = response["daily"]["temperature_2m_mean"]
        clean_temps = [t for t in temps if t is not None]

       
        start_temp = sum(clean_temps[:366]) / 366  
        end_temp = sum(clean_temps[-365:]) / 365

        
        return [start_temp, end_temp]

    except Exception as e:
        print("Error getting history:", e)
        return None

