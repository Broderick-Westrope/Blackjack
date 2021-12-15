class Hand:
    # Each card should be a tuple of the structure (card, value), where card is the literal card (ie. 2, A, K) and the value is the numeric value of that card (ie. 2, 11, 10)
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def splitHand(self):
        if len(self.cards) == 2 and self.cards[0] == self.cards[1]:
            choice = input("\nWould you like to split your pair? [Y/n]").upper()
            if choice != "N":
                newHand = Hand(self.cards.pop())
                return newHand
            else:
                return False

    def getLast(self):
        return self.cards[len(self.cards)-1]
