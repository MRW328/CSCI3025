import unittest
from main import get_coordinates


class TestGetCoordinates(unittest.TestCase):
    """Tests for the get_coordinates function in main.py."""

    def test_nonexistent_city_raises(self):
        """Looking up a fake city name should raise ValueError."""
        with self.assertRaises(ValueError):
            get_coordinates("zzznotacity")


if __name__ == "__main__":
    unittest.main()