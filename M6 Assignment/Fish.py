from Animal import Animal

class Fish(Animal):

    def __init__(self, name = "n/a", species = "n/a", ageInMonths = 0, waterType = "Salt", fed = False):
        """initializer

        Args:
            name (str, optional): name of fish. Defaults to "n/a".
            species (str, optional): species of fish. Defaults to "n/a".
            ageInMonths (int, optional): age in months. Defaults to 0.
            waterType (str, optional): water type of fish. Defaults to "Salt".
            fed (bool, optional): was the fish fed. Defaults to False.
        """
        super().__init__(name, species, ageInMonths)
        self.waterType = waterType
        self.fed = fed

    def feed(self):
        """function that checks if fish was fed.
           If not, feeds fish and sets fed to true
        """
        if self.fed == True:
            print(f'{self.name} has already been fed.')

        else:
            print(f"Feeding {self.name}")
            self.fed = True

    def isFed(self): 
        """
            returns fed status
        """      
        return self.fed
    
    def __str__(self):
        """returns string of Fish object

        Returns:
            Str: string of Fish object
        """
        return (f"{self.name} Species: {self.species} Months old: {self.age} Type: {self.waterType} Fed: {self.fed}")