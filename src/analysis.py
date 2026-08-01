def get_warming_summary(city_name, live_temp, history):
    """
    Creates a simple climate summary.
    """

    first = history[0]
    last = history[-1]

    change = round(last - first, 2)

    return (
        f"{city_name} is {live_temp}°C right now, "
        f"and has warmed {change}°C over the recorded period."
    )
