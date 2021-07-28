# nom du fichier (lower_snakecase) super_fish.py 
# nom de la classe (UpperCamelcase) SuperFish

class Animal:
    sleep_in = "Jungle"
    
    # constructor
    def __init__(self, name, race, color):
        self.race = race
        self.color = color
        self.name = name
        
    def talk(self, something):
        print(f"The {self.race} says '{something}'!")
        
    @classmethod
    def description_of_tribes(cls, tribes):
        for animal in tribes:
            print(f"- {animal.name} : {cls.sleep_in}")
            