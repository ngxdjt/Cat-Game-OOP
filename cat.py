class Cat:
    # Constructor
    # Creates a cat given its name and colour
    def __init__(self,givenName,givenColour):
        self.name = givenName
        self.colour = givenColour
        self.age = 1
        self.intelligence = 20
        self.energy = 15
        self.weight = 20

    def play(self):
        print(f"You play with {self.name}.")
        self.intelligence -= 5
        self.energy += 5
        self.weight -= 1

    def train(self):
        if self.energy >= 8:
            print(f"You train {self.name}")
            self.intelligence += 8
            self.energy -= 6
            self.weight -= 5
        else:
            print(f"{self.name} is too tired to train.")

    def feed(self):
        print(f"{self.name} ate a fish.")
        self.intelligence += 4
        self.energy += 2
        self.weight += 5

    def sleep(self):
        if self.energy <= 20:
            print(f"{self.name} rested on your lap")
            self.intelligence -= 1
            self.energy += 10
            self.weight += 3
        else:
            print(f"{self.name} has too much energy to fall asleep")
    
    def stats(self):
        print(f"Cat Attributes\nIntelligence: {self.intelligence}\nEnergy: {self.energy}\nWeight: {self.weight}")

    def checkDeath(self):
        if self.energy <= 5:
            print("Your cat died due to lack of energy")
            return False
        elif self.weight >= 50:
            print("Your cat died of obesity")
            return False
        elif self.weight <= 10:
            print("Your cat died of malnutrition")
            return False
        elif self.intelligence <= 5:
            print("Your cat died by getting hit by a car while crossing the road")
            return False
        else:
            return True
