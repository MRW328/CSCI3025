#super/parent class
class Animal:
    def __init__(self, name='aquariumFish', species = 'fish', ageInMonths = 0):
        """initializer for class

        Args:
            name (str, name of animal. Defaults to 'aquariumFish'.
            species (str, optional): species of animal. Defaults to 'fish'.
            ageInMonths (int, optional): age of animal. Defaults to 0.
        """
        self.name = name
        self.species = species
        self._ageInMonths = ageInMonths 

    @property
    def age(self):
        """gets ageInMonths

        Returns:
            int: age in months
        """
        return self._ageInMonths
    @age.setter
    def age(self, value):
        """sets ageInMonths

        Args:
            value int: age in months
        """
        if value < 0:
            print("Age cannot be negative")
        else:
            self._ageInMonths = value

    def __str__(self):
        """string

        Returns:
            string: Animal object
        """
        return (f"{self.name} Species: {self.species} Months old: {self.age}")