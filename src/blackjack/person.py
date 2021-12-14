class Person:
    def __init__(self, name, value):
        self.name = name
        self.value = value # This is the dollar ($) amount for the players chips

    def getHandTotal(self):
        total = 0
        for card in self.hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A" or card == 1: #! This needs to be made specific for each child class because players choose the value of A but dealer automates this
                if total >= 11: total += 1
                else: total += 11
            else:
                total += card
        return total

    def getHandString(self):
        string = ""
        size = len(self.hand)
        for i in range(size):
            string += str(self.hand[i])
            if i+1 < size:
                string += ", "
        return string

    def deal(self, game):
        self.hand = []
        for i in range(2): # Deal two cards
	        self.draw(game)

    def draw(self, game):
        card = game.getCard()
        if card == 11: card = "J"
        elif card == 12: card = "Q"
        elif card == 13: card = "K"
        elif card == 14: card = "A"
        self.hand.append(card)