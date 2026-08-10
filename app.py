import streamlit as st
from src import weather_data
from src import analysis
from src import climate

st.title("Climate Insight")

city = st.text_input("Type your city", "London")

if city:
    coordinates = weather_data.get_coordinates(city)

    if coordinates:
        lat, lon = coordinates

        st.write(f"Fetching climate data for {city}")

        live_data = weather_data.get_weather(lat, lon)

        if live_data is None:
            st.error("Couldn't fetch live weather for this location. Try a specific city instead of a country.")
        else:
            history_data = climate.get_climate_history(lat, lon)
            live_temp = live_data[0]

            result = analysis.get_warming_summary(
                city,
                live_temp,
                history_data
            )

            st.subheader("--- Climate Insight ---")
            st.write(result)

            if history_data:
                st.line_chart(history_data)

            st.subheader("Why does it matter?")
            st.write("Small shifts in average temperature affect rainfall patterns, heatwaves, and daily life in your city — seeing your own city's numbers makes climate change personal, not abstract.")

            st.subheader("What should I do?")
            for tip in analysis.get_action_tips():
                st.checkbox(tip)

    else:
        st.error("City not found")