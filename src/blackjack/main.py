import random
from utilities import clearCLI
from player import Player
from dealer import Dealer

deck = [0]

def printTitle(player, dealer):
    print("""
88          88                       88        88                       88
88          88                       88        ""                       88
88          88                       88                                 88
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[
B8b,   ,a8" R8 O8,    ,88 "Da,   ,aa E8`"Yba,  R8 I8,    ,88 "Ca,   ,aa K8`"Yba,
WY"Ybbd8"'  E8 `"SbbdP"Y8  `"Tbbd8"' R8   `Y8a O8 `"PbbdP"Y8  `"Ebbd8"' 88   `Y8a
                                              ,88
                                            888P"       \n
~ RULES ~
Decks: 6
Bet Min/Max: $1/$500

~ CHIPS ~
""" + player.name + """:\t $""" + str(player.value) + """
Dealer:\t $""" + str(dealer.value) + "\n")

def resetDeck(): # Reset & shuffle the deck
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*6
    random.shuffle(deck)
    return deck


def playAgain(player, dealer, deck):
    again = input("Do you want to play again? (Y/N) : ").upper()
    if again == "Y":
	    round(player, dealer, deck)
    else:
	    print("Bye!")
	    exit()


def printResults(dealer, player):
    print("~ RESULTS ~")
    print("Dealer:\t Holding ~ " + dealer.getHandString() + " ~ for a total of |" + str(dealer.getHandTotal()) + "|")
    print(player.name + ":\t Holding ~ " + player.getHandString() + " ~ for a total of |" + str(player.getHandTotal()) + "|")


def blackjack(dealer, player):
    if player.getHandTotal == 21:
        clearCLI()
        printResults(dealer.hand, player.hand)
        print("Congratulations! You got a Blackjack!\n")
        playAgain()
    elif dealer.getHandTotal == 21:
        clearCLI()
        printResults(dealer.hand, player.hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        playAgain()


def score(dealer, player):
    print("")
    dealerTotal = dealer.getHandTotal()
    playerTotal = player.getHandTotal()
    if playerTotal == 21:
        if dealerTotal == 21:
            printResults(dealer, player)
            print("It's a stand-off. You and the dealer got Blackjack.\n")
        else:
            calcWinnings = player.bet * 1.5
            player.value += calcWinnings
            dealer.value -= calcWinnings
            printResults(dealer, player)
            print("Congratulations! You got a Blackjack!\n")
    elif dealerTotal == 21:
        player.value -= player.bet
        dealer.value += player.bet
        printResults(dealer, player)
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif playerTotal > 21:
        player.value -= player.bet
        dealer.value += player.bet
        printResults(dealer, player)
        print("Sorry, you busted. You lose.\n")
    elif dealerTotal > 21:
        player.value += player.bet
        dealer.value -= player.bet
        printResults(dealer, player)
        print("Dealer busts. You win!\n")
    elif playerTotal < dealerTotal:
        player.value -= player.bet
        dealer.value += player.bet
        printResults(dealer, player)
        print("Sorry, your score is lower than the dealer. You lose.\n")
    elif playerTotal > dealerTotal:
        player.value += player.bet
        dealer.value -= player.bet
        printResults(dealer, player)
        print("Congratulations! Your score is higher than the dealer. You win\n")
    elif playerTotal == dealerTotal:
        printResults(dealer, player)
        print("It's a stand-off. You and the dealer tied.\n")



def game():
    deck = resetDeck()
    # Create players
    player = Player("Brodie", 2000)
    dealer = Dealer()
    
    round(player, dealer, deck)


def round(player, dealer, deck):
    clearCLI() # Clear output
    printTitle(player, dealer) # Print the "blackjack" title/ascii art

    player.getBet()
    player.deal(deck)
    dealer.deal(deck)

    # Loop the game
    while True:
        print("Dealer:\t Showing ~ " + str(dealer.hand[0]) + " ~")
        print(player.name + ":\t Holding ~ " + player.getHandString() + " ~ for a total of |" + str(player.getHandTotal()) + "|")
        blackjack(dealer, player)

        player.takeTurn(deck)
        dealer.takeTurn(deck)

        score(dealer, player)
        playAgain(player, dealer, deck)


	
if __name__ == "__main__":
    game()