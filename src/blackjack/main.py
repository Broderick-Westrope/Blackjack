# ANCHOR - Imports
import random
from utilities import clearCLI
from firstAI import FirstAI
from player import Player
from dealer import Dealer
from game import Game


# ANCHOR - Gameplay


def startMatch():
    game = Game()
    # Create players
    player = Player("Brodie", 2000, game)
    dealer = Dealer(game)
    round(player, dealer, game)


def round(player, dealer, game):
    printTitle(player, dealer)  # Print the "blackjack" title/ascii art
    player.getBet()
    printTitle(player, dealer, True)  # Print the "blackjack" title/ascii art

    player.deal()
    dealer.deal()

    # Loop the game
    while True:
        print("Dealer:\t Showing ~ " + str(dealer.getHandString()) + " ~")
        game.dealerUpCard = dealer.hands[0]
        print(player.name + ":\t Holding ~ " + player.getHandString() +
              " ~ for a total of |" + str(player.getHandTotal()) + "|")

        checkBlackjack(dealer, player, game)

        player.takeTurn()
        dealer.takeTurn()

        score(dealer, player, game)


def playAgain(player, dealer, game):
    again = input("Do you want to play again? (Y/N) : ").upper()
    if again == "Y":
        round(player, dealer, game)
    else:
        print("Bye!")
        exit()


# ANCHOR - Scoring


def score(dealer, player, game):
    print("")
    checkBlackjack(dealer, player, game)
    dealerTotal = dealer.getHandTotal()
    playerTotal = player.getHandTotal()

    if playerTotal > 21:
        player.value -= player.bet
        dealer.value += player.bet
        printResults(dealer, player)
        print("Sorry, you busted. You lose.\n")
        playAgain(player, dealer, game)
    elif dealerTotal > 21:
        player.value += player.bet
        dealer.value -= player.bet
        printResults(dealer, player)
        print("Dealer busts. You win!\n")
        playAgain(player, dealer, game)
    elif playerTotal < dealerTotal:
        player.value -= player.bet
        dealer.value += player.bet
        printResults(dealer, player)
        print("Sorry, your score is lower than the dealer. You lose.\n")
        playAgain(player, dealer, game)
    elif playerTotal > dealerTotal:
        player.value += player.bet
        dealer.value -= player.bet
        printResults(dealer, player)
        print("Congratulations! Your score is higher than the dealer. You win\n")
        playAgain(player, dealer, game)
    elif playerTotal == dealerTotal:
        printResults(dealer, player)
        print("It's a stand-off. You and the dealer tied.\n")
        playAgain(player, dealer, game)
    else:
        print("** ERROR: (main.py) Score reached unknown state. **")


def checkBlackjack(dealer, player, game):
    dealerTotal = dealer.getHandTotal()
    playerTotal = player.getHandTotal()

    if playerTotal == 21:
        if dealerTotal == 21:
            printResults(dealer, player)
            print("It's a stand-off. You and the dealer got Blackjack.\n")
            playAgain(player, dealer, game)
        else:
            calcWinnings = player.bet * 1.5
            player.value += calcWinnings
            dealer.value -= calcWinnings
            printResults(dealer, player)
            print("Congratulations! You got a Blackjack!\n")
            playAgain(player, dealer, game)
    elif dealerTotal == 21:
        player.value -= player.bet
        dealer.value += player.bet
        printResults(dealer, player)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        playAgain(player, dealer, game)


# ANCHOR - Printing

def printTitle(player, dealer, bet=False):
    clearCLI()
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
Dealer:\t $""" + str(dealer.value))
    if bet:
        print(player.name + """:\t $""" + str(player.value) +
              " (Betting $" + str(player.bet) + ")")
    else:
        print(player.name + """:\t $""" + str(player.value))
    print("")


def printResults(dealer, player):
    print("~ RESULTS ~")
    print("Dealer:\t Holding ~ " + dealer.getHandString() +
          " ~ for a total of |" + str(dealer.getHandTotal()) + "|")
    print(player.name + ":\t Holding ~ " + player.getHandString() +
          " ~ for a total of |" + str(player.getHandTotal()) + "|")


# ANCHOR - Initialization
if __name__ == "__main__":
    startMatch()
