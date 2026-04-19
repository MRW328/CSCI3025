#Matthew Williams
#CSCI 3025 - M9A1

class Location:
    """geographic location with coordinates"""

    def __init__(self, name, country, latitude, longitude, admin1=None):
        self.name = name
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.admin1 = admin1

    def __str__(self):
        if self.admin1:
            return f"{self.name}, {self.admin1}, {self.country} ({self.latitude}, {self.longitude})"
        return f"{self.name}, {self.country} ({self.latitude}, {self.longitude})"