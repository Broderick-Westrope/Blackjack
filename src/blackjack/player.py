from utilities import clearCLI, removeLine
from person import Person, Hand


class Player(Person):
    def __init__(self, name, value, game):
        super().__init__(name, value, game)

    def takeTurn(self):
        for hand in self.hands:  # Play each hand that this player controls
            self.playHand(hand)

    def playHand(self, hand):
        self.printHand(hand)
        if self.hands.index(hand) == 0:  # If this its the original two cards dealt
            if self.firstHand() == "Double":
                return

        # Play hand
        while True:
            total = self.getHandTotal(hand)
            if total > 21:
                print("Your hand went bust.")
            elif total == 21:
                print("Your hand got blackjack!")
            else:
                choice = input(
                    "Do you want to [H]it, [S]tand, or [Q]uit: ").upper()
                # ansi escape arrow up then overwrite the line
                removeLine()
                if choice == "H":
                    self.hit(hand)
                elif choice == "S":
                    break
                elif choice == "Q":
                    exit()

    def firstHand(self):
        hand = self.hands[0]
        total = self.getHandTotal(hand)
        # Split pairs
        result = self.splitHand(hand)
        if result != None:
            self.hands.append(result)
            self.printHand(hand)
            if hand.cards[0][0] == "A":
                self.hit(hand)
                return "Split"
        # Double down
        elif total == 9 or total == 10 or total == 11:
            if self.doubleDown() == True:  # If the player wants to double down
                self.hit(hand)  # Give them one final card
                return "Double"

    def hit(self, hand):
        card = self.draw()
        # If the card is an Ace
        if card == 14:
            card = "A"
            while True:
                value = input(
                    self.name + ":\t Got an Ace. Would you like this to a be worth 1 or 11? [1/11]")
                if value == "1":
                    card = 1
                    break
                elif value == "11":
                    break
        else:
            # Check if the card is a picture card
            if card == 11:
                card = "J"
            elif card == 12:
                card = "Q"
            elif card == 13:
                card = "K"
        # Add the card to the players hand
        hand.addCard(card)

        # Display draw & hands
        i = self.hands.index(hand)
        print(self.name + " (Hand " + str(i+1) + "):  Drew a " + str(card[0]))
        self.printHand(hand)

    def doubleDown(self):
        choice = input("\nWould you like to double down on your original bet of $" +
                       str(self.bet) + "? [y/N]").upper()
        if choice == "Y":
            self.bet *= 2
            return True

    def splitHand(self, hand):
        if len(hand.cards) == 2 and hand.cards[0] == hand.cards[1]:
            if hand.cards[0][0] == "A":
                print(
                    "NOTE: If you split your pair of Aces each hand will only get one more card on each hand.")
            choice = input("Would you like to split your pair of " +
                           str(hand.cards[0][0]) + "'s? [Y/n]").upper()
            removeLine()
            if choice != "N":
                print("Brodie split his pair (fix me)")
                newHand = Hand()
                newHand.addCard(hand.cards.pop())
                return newHand

    def getBet(self):
        bet = 1
        while True:
            try:
                value = input("How much would you like to bet? [1 - 500] ")
                bet = int(value)
                assert(1 <= bet and bet <= 500)
            except Exception:
                print(
                    "Please enter an integer between 1 and 500. This will be the dollar ($) value of your bet.")
                continue
            if self.value < bet:
                print("You only have $" + str(self.value) +
                      ". Please place an appropriate bet.")
            else:
                break
        self.bet = bet
