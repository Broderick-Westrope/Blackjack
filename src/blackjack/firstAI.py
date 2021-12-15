from utilities import clearCLI
from person import Person
from game import Game

class FirstAI(Person):
    def __init__(self, name, value, decks):
        super().__init__(name, value)
        self.decks = decks
        self.runningCount = 0
        self.trueCount = 0

    def takeTurn(self, game):
        if game.dealerUpCard == "J" or game.dealerUpCard == "Q" or game.dealerUpCard == "K":
            game.dealerUpCard = 10
        elif game.dealerUpCard == "A" or game.dealerUpCard == 1: #! This needs to be made specific for each child class because players choose the value of A but dealer automates this
            game.dealerUpCard = 11

        while True:
            total = self.getHandTotal()
            if total > 21:
                print("You went bust.")
                return
            elif total >= 17:
                return
            elif total <= 16 and total >= 13:
                if game.dealerUpCard <= 7:
                    return
            elif total == 12:
                if game.dealerUpCard <= 7 and game.dealerUpCard >= 4:
                    return
            self.hit(game)

    def hardTotal():
        pass

    def softTotal():
        pass


    def hit(self, game):
        card = game.getCard()
        # If the card is an Ace
        if card == 14:
            card = "A"
            while True:
                value = input(self.name + ":\t Got an Ace. Would you like it to be worth 1 or 11? [1/11]")
                if value == "1":
                    card = 1
                    break
                elif value == "11": break
        else:
            # Check if the card is a picture card
            if card == 11: card = "J"
            elif card == 12: card = "Q"
            elif card == 13: card = "K"
        # Add the card to the players hand
        self.hands.append(card)
        print(self.name + ":\t Picked up a " + str(card) + " for a total of |" + str(self.getHandTotal()) + "|")


    def getBet(self):
        self.bet = 20


    def calcTrueCount(self, dealerHand):
        count = 0
        for card in dealer.hand:
            if card == "J" or card == "Q" or card == "K" or card == "A" or card == 1: #! This needs to be made specific for each child class because players choose the value of A but dealer automates this
                count -= 1
            elif card >= 2 and card <= 6: 
                count += 1
        for card in self.hands:
            if card == "J" or card == "Q" or card == "K" or card == "A" or card == 1: #! This needs to be made specific for each child class because players choose the value of A but dealer automates this
                count -= 1
            elif card >= 2 and card <= 6: 
                count += 1
        self.runningCount += count
        self.trueCount = self.runningCount // self.decks