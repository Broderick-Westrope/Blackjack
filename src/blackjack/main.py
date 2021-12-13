import random
from utilities import clearCLI

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def printTitle():
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
                                            888P" \n""")

def deal(deck):
    hand = []
    for i in range(2): # Deal two cards
	    card = deck.pop()
	    if card == 11: card = "J"
	    if card == 12: card = "Q"
	    if card == 13: card = "K"
	    if card == 14: card = "A"
	    hand.append(card)
    return hand


def playAgain():
    again = input("Do you want to play again? (Y/N) : ").upper()
    if again == "Y":
	    dealerHand = []
	    playerHand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print("Bye!")
	    exit()


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11: total += 1
            else: total += 11
        else:
            total += card
    return total


def hit(hand):
	card = deck.pop()
	if card == 11: card = "J"
	if card == 12: card = "Q"
	if card == 13: card = "K"
	if card == 14: card = "A"
	hand.append(card)
	return hand


def handToString(hand):
    string = ""
    size = len(hand)
    for i in range(size):
        string += str(hand[i])
        if i+1 < size:
            string += ", "
    return string


def printResults(dealerHand, playerHand):
    print("")
    print("Dealer:\t Holding ~ " + handToString(dealerHand) + " ~ for a total of " + str(total(dealerHand)))
    print("You:\t Holding ~ " + handToString(playerHand) + " ~ for a total of |" + str(total(playerHand)) + "|")


def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		printResults(dealer_hand, player_hand)
		print("Congratulations! You got a Blackjack!\n")
		playAgain()
	elif total(dealer_hand) == 21:
		printResults(dealer_hand, player_hand)
		print("Sorry, you lose. The dealer got a blackjack.\n")
		playAgain()


def score(dealerHand, playerHand):
    print("")
    if total(playerHand) == 21:
        printResults(dealerHand, playerHand)
        print("Congratulations! You got a Blackjack!\n")
    elif total(dealerHand) == 21:
        printResults(dealerHand, playerHand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif total(playerHand) > 21:
        printResults(dealerHand, playerHand)
        print("Sorry, you busted. You lose.\n")
    elif total(dealerHand) > 21:
        printResults(dealerHand, playerHand)
        print("Dealer busts. You win!\n")
    elif total(playerHand) < total(dealerHand):
        printResults(dealerHand, playerHand)
        print("Sorry, your score isn't higher than the dealer. You lose.\n")
    elif total(playerHand) > total(dealerHand):
        printResults(dealerHand, playerHand)
        print("Congratulations! Your score is higher than the dealer. You win\n")


def playerTurn(hand):
    while total(hand) <= 21:
        choice = input("\nDo you want to [H]it, [S]tand, or [Q]uit: ").upper()
        clearCLI()
        if choice == "H":
            hit(hand)
            print("You:\t Picked up a " + str(hand[len(hand)-1]) + " for a total of |" + str(total(hand)) + "|")
        elif choice == "S":
            return
        elif choice == "Q":
            return "Q"
    else:
        print("You went bust.")
    

def dealerTurn(hand):
    print("")
    while total(hand) < 17:
        hit(hand)
        print("Dealer:\t Picked up a " + str(hand[len(hand)-1]) + " for a total of |" + str(total(hand)) + "|")


def game():
    choice = 0
    clearCLI() # Clear output
    printTitle() # Print the "blackjack" title/ascii art
    random.shuffle(deck) # Shuffle the deck

    # Deal hands
    dealerHand = deal(deck)
    playerHand = deal(deck)
    
    # Loop the game
    while choice != "Q":
        print("Dealer:\t Showing a " + str(dealerHand[0]))
        print("You:\t Holding ~ " + handToString(playerHand) + " ~ for a total of |" + str(total(playerHand)) + "|")
        blackjack(dealerHand, playerHand)

        result = playerTurn(playerHand)
        if result != None:
            print("Bye!")
            exit()
        else:
            dealerTurn(dealerHand)
            score(dealerHand, playerHand)
            playAgain()

	
if __name__ == "__main__":
   game()