import requests


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
        response = requests.get(
            endpoint,
            params=info,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        dates = data["daily"]["time"]
        temps = data["daily"]["temperature_2m_mean"]

        yearly_data = {}

        # Step 1: Group temperatures by year
        for date, temp in zip(dates, temps):

            if temp is None:
                continue

            year = date[:4]

            if year not in yearly_data:
                yearly_data[year] = []

            yearly_data[year].append(temp)

        # Step 2: Calculate average for each year
        yearly_averages = {}

        for year, temperatures in yearly_data.items():

            average = sum(temperatures) / len(temperatures)

            yearly_averages[year] = average

        return yearly_averages

    except Exception as e:
        print("Error getting history:", e)
        return None