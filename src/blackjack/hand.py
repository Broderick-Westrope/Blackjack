class Hand:
    # Each card should be a tuple of the structure (card, value), where card is the literal card (ie. 2, A, K) and the value is the numeric value of that card (ie. 2, 11, 10)
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getLast(self):
        return self.cards[len(self.cards)-1]
