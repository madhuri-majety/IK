"""
Dealer cards
Player cards
Deal the cards for dealer
Display the last dealer card
Deal the cards for player
Sum of the dealer cards
Sum of the player cards
Compare the sums of the cards between D v P
If P card sum is greater than 21 = BUST
If P card sum is less than 21 = Option Hit or Stay
If P option Stay compare sum of D v P
If P sum < 21 && > D sum then P wins!
If P sum < D sum then P loses

https://www.youtube.com/watch?v=yJz2at4Hco4

https://github.com/techBytesIO/python_command_line/blob/master/blackjack.py

"""

import random

# Dealer cards
dealer_cards = []

# Player cards
player_cards = []

# Deal the cards for the dealer
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealers last card is : {}".format(dealer_cards[1]))

# Deal the cards for the player
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have : {}".format(player_cards))

# Sum the dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# Sum the player cards
while sum(player_cards) < 21:
    action = str(input("Do you want to stay or hit? "))
    if action == 'hit':
        player_cards.append(random.randint(1,11))
        print("You now have a total of {} from these cards {}".format(str(sum(player_cards)), player_cards))
    else:
        print("The dealer has a total of {} with these cards {}".format(str(sum(dealer_cards)), dealer_cards))
        print("You now have a total of {} from these cards {}".format(str(sum(player_cards)), player_cards))

        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You Win!")
            break

if sum(player_cards) == 21:
    print("You have Blackjact and you Win!")
elif sum(player_cards) > 21:
    print("You Busted! Dealer wins")





