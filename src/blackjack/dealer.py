from person import Person

class Dealer(Person):
    def __init__(self):
        super().__init__("Dealer", 4000)

    def takeTurn(self, game):
        while self.getHandTotal() < 17:
            self.draw(game)
            print("Dealer:\t Picked up a " + str(self.hand[len(self.hand)-1]) + " for a total of |" + str(self.getHandTotal()) + "|")