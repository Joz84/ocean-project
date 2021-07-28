from ocean.animal import Animal

class Lion(Animal):
    def __init__(self, name, color, fin_nbr):
        super().__init__(name, "lion", color)
        self.fin_nbr = fin_nbr
        
    def bouffe_une_gazelle():
        print("miam")