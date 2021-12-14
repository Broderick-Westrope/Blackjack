from utilities import clearCLI
from person import Person

class Player(Person):
    def __init__(self, name, value, game):
        super().__init__(name, value, game)

    def takeTurn(self):
        if self.hand[0] == self.hand[1]:
            self.splitPair()

        total = self.getHandTotal()
        if total == 9 or total == 10 or total == 11:
            if self.doubleDown(game) == True: return

        while self.getHandTotal() <= 21:
            choice = input("\nDo you want to [H]it, [S]tand, or [Q]uit: ").upper()
            clearCLI()
            if choice == "H":
                self.hit()
            elif choice == "S":
                return
            elif choice == "Q":
                exit()
        else:
            print("You went bust.")

    def hit(self):
        card = self.game.getCard()
        # If the card is an Ace
        if card == 14:
            card = "A"
            while True:
                value = input(self.name + ":\t Got an Ace. Would you like this to a be worth 1 or 11? [1/11]")
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
        self.hand.append(card)
        print(self.name + ":\t Picked up a " + str(card) + " for a total of |" + str(self.getHandTotal()) + "|")


    def splitPair(self):
        choice = input("\nWould you like to split your pair? [Y/n]").upper()
        if choice != "N":
            pass
    
    def doubleDown(self):
        choice = input("\nWould you like to double down on your original bet of " + str(self.bet) + "? [y/N]").upper()
        if choice == "Y":
            self.bet = int(self.bet * 2)
            self.hit()
            return True


    def getBet(self):
        bet = 1
        while True:
            try:
                value = input("How much would you like to bet? [1 - 500] ")
                bet = int(value)
                assert(1 <= bet and bet <= 500)
            except Exception:
                print("Please enter an integer between 1 and 500. This will be the dollar ($) value of your bet.")
                continue
            if self.value < bet:
                print("You only have $" + str(self.value) + ". Please place an appropriate bet.")
            else:
                break
        self.bet = bet