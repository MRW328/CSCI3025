import unittest

from location import Location

class TestLocation(unittest.TestCase):
    """Tests for the Location class"""

    def test_create_location(self):
        """A location should store the values passed to its constructor"""
        
        loc = Location("Albany", "United States", 42.65, -73.76)
        self.assertEqual(loc.name, "Albany")
        self.assertEqual(loc.country, "United States")
        self.assertEqual(loc.latitude, 42.65)
        self.assertEqual(loc.longitude, -73.76)
    
    def test_string_representation(self):
        """The __str__ method should produce a readable label."""

        loc = Location("Tokyo", "Japan", 35.68, 139.69)
        result = str(loc)
        self.assertIn("Tokyo", result)
        self.assertIn("Japan", result)

    def test_negative_coordinates(self):
        """Locations in southern/western hemispheres should work fine."""

        loc = Location("Sydney", "Australia", -33.87, 151.21)
        self.assertEqual(loc.latitude, -33.87)

    def test_location_equator(self):
        """Coordinates at zero (equator/prime meridian) should be valid."""

        loc = Location("Null Island", "None", 0.0, 0.0)
        self.assertEqual(loc.latitude, 0.0)
        self.assertEqual(loc.longitude, 0.0)

if __name__ == "__main__":
    unittest.main()