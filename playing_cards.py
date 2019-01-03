# from https://github.com/eli-byers/Deck-Of-Cards-Python/blob/master/deckofcards.py
# and https://www.youtube.com/watch?v=62TmpPDs0mM

from enum import Enum, IntEnum
import random

full_deck = []
# partial_deck = []
player1_cards = []
player2_cards = []

# card value enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

# suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

# class to hold information for playing cards
class PlayingCards:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

class Deck:
    def __init__(self):
        self.full_deck = []
        self.create_deck()
        self.partial_deck = list(full_deck)

    # creating full_deck
    def create_deck(self):
        for suit in Suit:
            for card in Card:
                full_deck.append(PlayingCards(Card(card), Suit(suit)))
        return full_deck

    # shuffle the deck
    def shuffle_deck(self, num = 1):
        length = len(self.partial_deck)

        for _ in range(num):
            for i in range(length - 1, 0, -1): # fisher yates shuffle algorithm
                randI = random.randint(0, i)

                if randI == i:
                    continue
                self.partial_deck[i], self.partial_deck[randI] = self.partial_deck[randI], self.partial_deck[i]
        # alternatively, we can create a shuffling algo by using random.shuffle
        # random.shuffle(self.partial_deck)

    # draw a card form the deck
    def draw_card(self, deck):
        # return deck.pop(random.randint(0, len(deck)-1)) # if deck in not suffled, pop out a random card
        # if deck is shuffled, simply pop
        return deck.pop()

    # deal equal numbers of random cards to two players for a game of WAR
    def deal_cards(self):
        player1_cards.append(self.draw_card(self.partial_deck))
        player2_cards.append(self.draw_card(self.partial_deck))


deck = Deck()
deck.deal_cards()

# imitating WAR
for i in range(0, len(player1_cards)):
    if player1_cards[i].card > player2_cards[i].card:
        print("player1 won the hand with card:", player1_cards[i].card)
        print("player2 lost the hand with card:", player2_cards[i].card)
    elif player1_cards[i].card < player2_cards[i].card:
        print("player2 won the hand with card:", player2_cards[i].card)
        print("player1 lost the hand with card:", player1_cards[i].card)
    else:
        print("WARRRR")



# test_card = draw_card(partial_deck)
# print(test_card.card, test_card.suit)


# printing all cards
# for i in range(0, len(full_deck)):
#     print("{} of {}".format(full_deck[i].card, full_deck[i].suit))
    # print(full_deck[i].card,'of', full_deck[i].suit)