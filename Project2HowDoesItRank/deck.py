import card as c
import random

LEAST_NUM_CARDS_TO_MAKE_DECK = 5
LOWEST_RANK = 2
HIGHEST_RANK_ACE = 14


class Deck:

    def __init__(self):
        """
        Constructs a deck. Creates, and shuffles the deck.
        """
        self.__card_deck = []
        self.create()
        self.__shuffle()

    def create(self):
        """
        Creates a deck of card and appends it to card deck list
        """
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        for suit in suits:
            for rank in range(LOWEST_RANK, HIGHEST_RANK_ACE + 1):
                self.__card_deck.append(c.Card(rank, suit))

    def __shuffle(self):
        random.shuffle(self.__card_deck)

    def num_cards_in_deck(self):
        """
        Determines the length of the deck
        :return: length of deck
        """
        return len(self.__card_deck)

    def less_than_5_cards(self):
        """
        Checks whether the deck has less than 5 cards
        :return: True iff length of deck is less than 5
        """
        return len(self.__card_deck) < LEAST_NUM_CARDS_TO_MAKE_DECK

    def deal_card(self):
        """
        Pops the last card in the deck
        :return: the card that was popped
        """
        return self.__card_deck.pop()

    def __str__(self):
        deck_string = ''
        for card in self.__card_deck:
            deck_string += card.__str__()
            deck_string += '\n'
        return deck_string
