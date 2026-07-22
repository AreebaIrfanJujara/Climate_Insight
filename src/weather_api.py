import requests
def get_coordinates(name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    extra = {
        "city_name": name,
        "count": 1
     }

    response=requests.get(url,params=extra)

    if response.statuscode==200:
        data=response.json()
        if data["results"]:
            return data["results"][0]["latitude"], data["results"][0]["longitude"]
        else:
            return None





