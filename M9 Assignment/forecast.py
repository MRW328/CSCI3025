
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

class Forecast:
    """daily forecast for a specific location"""

    def __init__(self, location, api_data):
        self.location = location #composition over inheritance 
        self.dates = api_data["daily"]["time"]
        self.temps = api_data["daily"]["temperature_2m_max"]

    
    def __str__(self):
        return f"{len(self.dates)}-day forecast for {self.location}"


    def print_table(self):
        for date, temp, in zip(self.dates, self.temps):
            print(f"{date}: {temp}F")    

    def to_dataframe(self):
        df = pd.DataFrame({
            "date": self.dates, 
            "temp":self.temps
        })
        return df


    def plot(self, filename):
        """Saves a PNG chart of the daily high temperatures"""
        df = self.to_dataframe()
    
        plt.figure(figsize=(10, 6))
        plt.plot(df["date"], df["temp"], marker="o")
        plt.title(f"7-Day High temperature for {self.location}")
        plt.xlabel("Date")
        plt.ylabel("High Temperature (F)")
        plt.grid(True)
        plt.xticks(rotation=45)         
        plt.tight_layout()     

        plt.savefig(filename)
        plt.close()    

        print(f"Chart saved to {filename}")
    

    def summary(self):
        """Print summary statistics for this forecast."""
        df = self.to_dataframe()

        avg_temp = df["temp"].mean()
        max_temp = df["temp"].max()
        min_temp = df["temp"].min()

        warmest_row = df["temp"].idxmax()
        warmest_date = df.loc[warmest_row, "date"]

        print(f"Summary for {self.location.name}:")
        print(f"7 day Average high: {avg_temp:.1f}F")
        print(f"7 day Highest high: {max_temp:.1f}F")
        print(f"7 day Lowest high : {min_temp:.1f}F")
        print(f"Warmest: {warmest_date} ({max_temp:.1f}F)")