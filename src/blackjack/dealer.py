from person import Person

class Dealer(Person):
    def __init__(self, game):
        super().__init__("Dealer", 4000, game)

    def takeTurn(self):
        while self.getHandTotal() < 17:
            self.draw()
            print("Dealer:\t Picked up a " + str(self.hand[len(self.hand)-1]) + " for a total of |" + str(self.getHandTotal()) + "|")