def get_warming_summary(city_name, live_temp, history):
    """
    Creates a simple climate summary.
    """

    if not history:
        return f"No historical climate data available for {city_name}."

    years = sorted(history.keys())

    first_year = years[0]
    last_year = years[-1]

    first_temp = history[first_year]
    last_temp = history[last_year]

    change = round(last_temp - first_temp, 2)

    if change > 0:
        return (
            f"{city_name} is {live_temp}°C right now, "
            f"and has warmed {change}°C from {first_year} to {last_year}."
        )

    elif change < 0:
        return (
            f"{city_name} is {live_temp}°C right now, "
            f"and has cooled {abs(change)}°C from {first_year} to {last_year}."
        )

    return (
        f"{city_name} is {live_temp}°C right now, "
        f"with almost no temperature change from {first_year} to {last_year}."
    )
    
