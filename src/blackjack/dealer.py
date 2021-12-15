from person import Person


class Dealer(Person):
    def __init__(self, game):
        super().__init__("Dealer", 4000, game)

    # TODO - The dealer shouldn't need to do anything if the player's hands have all busted
    def takeTurn(self):
        self.printHand()

        while self.getHandTotal() < 17:
            card = self.draw()
            self.hands[0].addCard(card)
            print("Dealer:\t Drew a " + str(card[0]))
            self.printHand()

    def getHandTotal(self):
        return super().getHandTotal(self.hands[0])

    def getHandString(self):
        return super().getHandString(self.hands[0])

    def topCard(self):
        return str(self.hands[0].cards[0][0])

    def printHand(self):
        print("Dealer:  Holding ~ " +
              self.getHandString() + " ~ for a total of |" + str(self.getHandTotal()) + "|\n")
