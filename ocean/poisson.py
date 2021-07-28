from ocean.animal import Animal

class Poisson(Animal):
    def __init__(self, name, color, fin_nbr, race="poisson"):
        super().__init__(name, race, color)
        self.place = "ocean"        
        self.fin_nbr = fin_nbr