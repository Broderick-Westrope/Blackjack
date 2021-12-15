from hand import Hand


class Person:
    def __init__(self, name, value, game):
        self.name = name
        self.value = value  # This is the dollar ($) amount for the players chips
        self.game = game
        self.hands = []

    def getHandTotal(self, hand):
        total = 0
        for card in hand.cards:
            total += card[1]
        return total

    def getHandString(self, hand):
        string = ""
        size = len(hand.cards)
        for i in range(size):
            string += str(hand.cards[i][0])
            if i+1 < size:
                string += ", "
        return string

    def deal(self):
        self.hands = []
        hand = Hand()
        for i in range(2):  # Deal two cards
            hand.addCard(self.draw())
        self.hands.append(hand)

    def draw(self):
        card = self.game.getCard()
        if card == 11:
            card = ("J", 10)
        elif card == 12:
            card = ("Q", 10)
        elif card == 13:
            card = ("K", 10)
        elif card == 14:
            card = ("A", 11)
        else:
            card = (card, card)
        return card

    def printHand(self, hand):
        i = self.hands.index(hand)
        print(self.name + " (Hand " + str(i+1) + "):  Holding ~ " +
              self.getHandString(hand) + " ~ for a total of |" + str(self.getHandTotal(hand)) + "|")
