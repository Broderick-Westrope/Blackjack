import random


class Game:
    def __init__(self):
        self.resetDeck()
        self.dealerUpCard = 0

    def resetDeck(self):  # Reset & shuffle the deck
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*6
        random.shuffle(self.deck)

    def getCard(self):
        if len(self.deck) == 0:
            self.resetDeck()
        card = self.deck.pop()
        return card
