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




