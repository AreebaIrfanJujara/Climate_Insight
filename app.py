from src import weather_api
from src import analysis


city = "London"

coordinates = weather_api.get_coordinates(city)

if coordinates:

    lat, lon = coordinates

    print(f"Fetching climate data for {city}")

    live_data = weather_api.get_weather(lat, lon)

    history_data = weather_api.get_climate_history(lat, lon)

    live_temp = live_data[0]

    result = analysis.get_warming_summary(
        city,
        live_temp,
        history_data
    )

    print("\n--- Climate Insight ---")
    print(result)

else:
    print("City not found")