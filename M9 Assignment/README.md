# Weather Forecast Analyzer

This program takes in user input for city and outputs and image for the 7-day average high temperature forecast of that city.

## Features

- Looks up any city by name using the Open-Meteo geocoding API
- prints a 7-day high temperature forecast and computes the average high and low temperatures for the next 7 days
- Saves a temperature trend chart to `forecast.png`
- Handles errors like connection error, invalid user input, timeout and http error

## Installation

1. Requires Python 3.10 or newer.
2. Install dependencies:

```
   pip install requests pandas matplotlib
```

No API key is needed — Open-Meteo is free for non-commercial use.

## Usage

Run the program from the project folder:

```
python main.py
```

You'll be asked to enter a city name. Here's an example run:

```
Enter the name of the city: Albany
7-day forecast for Albany
2026-04-19: 56.3F
2026-04-20: 43.4F
2026-04-21: 54.5F
2026-04-22: 56.3F
2026-04-23: 62.1F
2026-04-24: 60.8F
2026-04-25: 63.5F
Summary for Albany:
7 day average high: 56.7F
High:    63.5F
Low:     43.4F
Warmest: 2026-04-25 (63.5F)
Chart saved to forecast.png
```

A chart is saved as `forecast.png` in the same folder.

## Running the tests

From the project root:

```
python -m unittest discover -s tests -v
```

10 tests cover the Location and Forecast classes, including edge cases like negative coordinates, zero coordinates, and malformed API data.

## File Structure

```
M9 Assignment/
├── main.py         # program entry point. handles input, API calls, errors
├── location.py     # Location class (holds coordinates for a city)
├── forecast.py     # Forecast class (analysis, stats, chart)
└── tests/          # unit tests
    ├── test_location.py
    ├── test_forecast.py
    └── test_main.py
```
I plit this into multiple files so each one has a single responsibility. location.py and forecast.py each contain one class, which keep the program modular and easier for me to understand as I worked through it.


## Libraries used

- **requests** — HTTP calls to the open meteo API
- **pandas** — for building Dataframe and computing summary stats
- **matplotlib** — rendering graph and saving as PNG

## API credit

Weather data from [Open-Meteo](https://open-meteo.com/).

## Author

Matthew Williams — CSCI 3025



