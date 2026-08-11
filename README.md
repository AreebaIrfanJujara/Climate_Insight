# 🌍 Climate Insight

> A human-centered climate visualization prototype that answers three simple questions: **What is happening? Why does it matter? What should I do?**

**Live Demo:** https://climateinsight-areebairfanjujara.streamlit.app/

**Demo Video:** https://drive.google.com/file/d/1ts-c-f9SKR61LP-2UUaJ_oInt6GbjFWw/view?usp=sharing

---

## ❗ Problem Statement

Climate data is everywhere, but most of it is presented as dense charts, spreadsheets, or scientific jargon. This makes it hard for **children, students, commuters, and older adults** to understand what is actually happening to the climate, why it matters to their daily lives, and what — if anything — they can personally do about it.

## 💡 Solution Overview

**Climate Insight** lets a user type their **city**, then fetches **live weather** and **historical climate data** for that exact location in real time from the Open-Meteo API — no downloaded files, no outdated numbers. That data is translated into three plain-language layers, built around one guiding principle:

1. **What is happening?** — a clear, factual summary in everyday language.
2. **Why does it matter?** — short, honest context connecting the data to real life.
3. **What should I do?** — realistic, achievable actions anyone can take.

The result is a lightweight, accessible web app that anyone — regardless of age or technical background — can open and understand in under a minute.

## ✨ Key Features

- 📍 **Type your city** — no manual data files, works for (almost) any location on Earth.
- 🌤️ **Live current weather** for that exact location, fetched in real time from the Open-Meteo API.
- 📈 **Historical climate trend** for the same location — how temperatures there have shifted over recent decades.
- 🗣️ **Plain-English climate summaries** generated from real data, not jargon.
- ✅ **Actionable, checkable tips** so users leave with something to *do*, not just read.
- ⚡ **Fast, lightweight prototype** — no login, no downloaded dataset, no API key required.

## 🛠️ Technologies Used

- **Python 3.11+**
- **[requests](https://docs.python-requests.org/)** — fetching live data from the internet
- **[Open-Meteo API](https://open-meteo.com/)** — free, no-key API for live weather, geocoding, and historical climate data
- **[Streamlit](https://streamlit.io/)** — web interface
- **Git & GitHub** — version control and hosting
- **Streamlit Community Cloud** — free deployment

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
git clone <repository-link>
cd climate-insight
pip install -r requirements.txt
```

## ▶️ How to Run

```bash
streamlit run app.py
```

This opens the app automatically in your browser at `http://localhost:8501`.

## 🧭 Usage

1. Open the app in your browser (or visit the live demo link above).
2. **Type your city name.**
3. The app fetches your city's coordinates, then pulls **live weather** and **historical climate data** for that exact location.
4. Read **"What is happening?"** for a plain-language summary of current and historical conditions there.
5. Read **"Why does it matter?"** for quick, honest context.
6. Check off items under **"What should I do?"** to track small actions you're taking.
7. Explore the chart to see how temperatures in your area have changed over time.

## 📁 Project Structure

climate-insight/

├── app.py # Main Streamlit entry point

├── src/

│ ├── init.py

│ ├── weather_data.py # Fetches coordinates & live weather from Open-Meteo

│ ├── analysis.py # Turns data into plain-English insight sentences & action tips

│ └── climate.py # Fetches and processes historical climate data
├── requirements.txt
├── .gitignore
└── README.md


> Note: this project has **no local dataset file**. All weather and climate data is fetched live, on demand, from the Open-Meteo API each time a user searches a location.

## 🚧 Future Improvements

- 🌐 Dropdown of popular cities for quicker selection
- 🗣️ Multi-language support for wider accessibility
- ♿ Accessibility testing with real older-adult and child users
- 📊 Additional datasets (sea level, extreme weather frequency, CO₂ emissions)

## 👤 Author

**Areeba Irfan Jujara**





