from person import Person


class Dealer(Person):
    def __init__(self, game):
        super().__init__("Dealer", 4000, game)

    def takeTurn(self):
        while self.getHandTotal() < 17:
            self.hands[0].addCard(self.draw())
            print("Dealer:\t Picked up a " +
                  str(self.hands[0].getLast()[0]) + " for a total of |" + str(self.getHandTotal()) + "|")
