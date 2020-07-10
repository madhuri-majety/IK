"""
Implement classes for Python Deck of cards

Deck of cards program has three main real time entities
- Card
    - Every card has a suit and value associated with it
- Deck
    - Build 52 cards  - 13 cards of each suit
    - Shuffle the cards
    - Draw a card
    - Show the deck of cards
- Player
    - Has a hand
    - Can draw the cards to hand
    - discard cards


https://www.youtube.com/watch?v=t8YkjDH86Y4
https://github.com/eli-byers/Deck-Of-Cards-Python/blob/master/deckofcards.py
"""
import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    # Implementing built in methods so taht you can print a card object
    def __unicode__(self):
        return self.showCard()

    def __str__(self):
        return self.showCard()

    def __repr__(self):
        return self.showCard()

    def showCard(self):
        """
        Method __str__ should return string, not print
        :return:
        """
        if self.val == 1:
            val = "Ace"
        elif self.val == 11:
            val = "Jack"
        elif self.val == 12:
            val = "Queen"
        elif self.val == 13:
            val = "King"
        else:
            val = self.val

        return "{} of {}".format(val, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        # By instantiating the Deck object we want to build the deck of cards, so calling build() function
        # as part of constructor
        self.buildDeck()

    def buildDeck(self):
        """
        Generate 52 cards
        :return:
        """
        for suit in ['Heards', 'Spade', 'Diamonds', 'Clubs']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def showDeck(self):
        for card in self.cards:
            print(card)

    def shuffle(self, num=1):
        """
        Deck of cards should be able to shuffle.
        :return:
        """
        for time in range(num):
            # This is fisher yates shuffle algorithm
            for i in range(len(self.cards)-1, 0, -1):
                r = random.randint(0, i)

                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self):
        return self.cards.pop()



class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num = 1):
        for _ in range(num):
            self.hand.append(deck.deal())

    def showHand(self):
        print("{}'s hand: {}".format(self.name, self.hand))

    def discard(self):
        self.hand.pop()


def main():
    myDeck = Deck()
    myDeck.shuffle()
    myDeck.showDeck()

    madhu = Player("Madhu")
    madhu.draw(myDeck, 10)
    madhu.showHand()

if __name__ == '__main__':
    main()
