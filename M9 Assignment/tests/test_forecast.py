import unittest
from location import Location
from forecast import Forecast

#python -m unittest discover -s tests -v
class TestForecast(unittest.TestCase):
    """Tests for the Forecast class."""

    
    def setUp(self):
        """Build a sample Location and fake API response for use in tests.
        
        setUp runs before each test method, so every test starts
        with the same data.
        """
        self.location = Location("Albany", "United States", 42.65, -73.76)
        
        self.fake_api_data = {
            "daily": {
                "time": ["2026-04-18", "2026-04-19", "2026-04-20"],
                "temperature_2m_max": [70.0, 75.0, 65.0],
            }
        }

   
    def test_forecast_stores_location(self):
        """The forecast should hold onto the location it was given."""

        forecast = Forecast(self.location, self.fake_api_data)
        self.assertEqual(forecast.location.name, "Albany")

    
    def test_forecast_extracts_dates(self):
        """The forecast should pull dates out of the API data."""
        
        forecast = Forecast(self.location, self.fake_api_data)
        self.assertEqual(forecast.dates, ["2026-04-18", "2026-04-19", "2026-04-20"])

   
    def test_forecast_extracts_temps(self):
        """The forecast should pull temperatures out of the API data."""
       
        forecast = Forecast(self.location, self.fake_api_data)
        self.assertEqual(forecast.temps, [70.0, 75.0, 65.0])
   
   
    def test_dataframe_columns(self):
        """to_dataframe should produce a DataFrame with date and temp columns."""
       
        forecast = Forecast(self.location, self.fake_api_data)
        df = forecast.to_dataframe()
        self.assertIn("date", df.columns)
        self.assertIn("temp", df.columns)
        self.assertEqual(len(df), 3)


    def test_forecast_with_bad_data_raises(self):
        """Constructing a Forecast with malformed API data should raise KeyError."""
       
        bad_data = {"daily": {}}    # missing the expected 'time' and 'temperature_2m_max' keys
       
        with self.assertRaises(KeyError):
            Forecast(self.location, bad_data)

if __name__ == "__main__":
    unittest.main()