from weather_api import get_weather


print("🌍 Climate Insight Started")


weather = get_weather(24.8607, 67.0011)  # Karachi coordinates

print(weather)