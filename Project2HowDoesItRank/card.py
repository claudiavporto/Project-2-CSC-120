JACK = 11
QUEEN = 12
KING = 13
ACE = 14


class Card:

    def __init__(self, rank, suit):
        """
        Constructs a card with a given rank and suit.
        :param rank: The given rank
        :param suit: The given suit
        """
        self.__rank = rank
        self.__suit = suit

    def get_rank(self):
        """
        Gets and returns the rank of the card.
        :return: The rank
        """
        return self.__rank

    def get_suit(self):
        """
        Gets and returns the suit of the card.
        :return: The suit
        """
        return self.__suit

    def __str__(self):
        str_rank = ''
        if self.__rank == JACK:
            str_rank = 'Jack'
        elif self.__rank == QUEEN:
            str_rank = 'Queen'
        elif self.__rank == KING:
            str_rank = 'King'
        elif self.__rank == ACE:
            str_rank = 'Ace'
        else:
            str_rank = str(self.__rank)
        return f'{str_rank} of {self.__suit}'

