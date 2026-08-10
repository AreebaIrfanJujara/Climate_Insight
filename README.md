# 🌍 Climate Insight

> A human-centered climate visualization prototype that answers three simple questions: **What is happening? Why does it matter? What should I do?**

**Live Demo:** `<paste your Streamlit Community Cloud link here once deployed>`

**Demo Video:** `<paste your 1–2 min screen recording link here (YouTube/Loom/Drive)>`
---

## ❗ Problem Statement

Climate data is everywhere, but most of it is presented as dense charts, spreadsheets, or scientific jargon. This makes it hard for **children, students, commuters, and older adults** to understand what is actually happening to the climate, why it matters to their daily lives, and what — if anything — they can personally do about it.

## 💡 Solution Overview

**Climate Insight** lets a user type or select their **city or region**, then fetches **live weather** and **historical climate data** for that exact location in real time from the Open-Meteo API — no downloaded files, no outdated numbers. That data is translated into three plain-language layers, built around one guiding principle:

1. **What is happening?** — a clear, factual summary in everyday language.
2. **Why does it matter?** — short, honest context connecting the data to real life.
3. **What should I do?** — 2–3 realistic, achievable actions anyone can take.

The result is a lightweight, accessible web app that anyone — regardless of age or technical background — can open and understand in under a minute.

## ✨ Key Features

- 📍 **Type your city, or pick one from a dropdown** — no manual data files, works for (almost) any location on Earth.
- 🌤️ **Live current weather** for that exact location, fetched in real time from the Open-Meteo API.
- 📈 **Historical climate trend** for the same location — how temperatures there have shifted over recent decades.
- 🗣️ **Plain-English climate summaries** generated from real data, not jargon.
- ✅ **Actionable, checkable tips** so users leave with something to *do*, not just read.
- 🎨 **Accessible design** — large fonts, calm colors, simple layout for all ages.
- ⚡ **Fast, lightweight prototype** — no login, no downloaded dataset, no API key required.

## 🖼️ Screenshots

| Home View | Insight & Chart | Action Tips |
|---|---|---|
| ![Home](assets/images/screenshot-home.png) | ![Insight](assets/images/screenshot-insight.png) | ![Tips](assets/images/screenshot-tips.png) |

*(Replace the images above with your own screenshots saved in `assets/images/`.)*

## 🛠️ Technologies Used

- **Python 3.11+**
- **[requests](https://docs.python-requests.org/)** — fetching live data from the internet
- **[Open-Meteo API](https://open-meteo.com/)** — free, no-key API for live weather, geocoding, and historical climate data
- **[pandas](https://pandas.pydata.org/)** — organizing and analyzing the fetched data
- **[NumPy](https://numpy.org/)** — numerical calculations
- **[Matplotlib](https://matplotlib.org/)** — data visualization / charts
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

1. Open the app in your browser.
2. **Type your city name**, or pick one from the **dropdown of popular cities**.
3. The app fetches your city's coordinates, then pulls **live weather** and **historical climate data** for that exact location.
4. Read **"What is happening?"** for a plain-language summary of current and historical conditions there.
5. Read **"Why does it matter?"** for quick, honest context.
6. Check off items under **"What should I do?"** to track small actions you're taking.
7. Explore the chart to see how temperatures in your area have changed over time.

## 📁 Project Structure

```
climate-insight/
├── app.py                 # Main Streamlit entry point
├── src/
│   ├── __init__.py
│   ├── weather_data.py    # Fetches coordinates & live weather from Open-Meteo
│   ├── analysis.py        # Turns data into plain-English insight sentences
│   └── climate.py         # Fetches and processes historical climate data
├── requirements.txt
├── .gitignore
└── README.md
```

> Note: this project has **no local dataset file**. All weather and climate data is fetched live, on demand, from the Open-Meteo API each time a user searches a location.

## 🚧 Future Improvements

- 🌐 Location-based climate data (city/country-level insights)
- 🗣️ Multi-language support for wider accessibility
- ♿ Accessibility testing with real older-adult and child users
- 📊 Additional datasets (sea level, extreme weather frequency, CO₂ emissions)


## 👤 Author

**`<Your Name>`**
`<your email / LinkedIn / portfolio link>`

---

*Built as part of a 6-day guided learning sprint focused on human-centered design and clean software engineering fundamentals.*
