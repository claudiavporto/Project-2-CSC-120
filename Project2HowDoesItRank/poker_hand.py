import test_suite as test
import card as c

HAND_1_WINS = 1
TIE = 0
HAND_2_WINS = -1
NUM_CARDS_IN_HAND = 5
NUM_HIGH_CARDS_PAIR = 3
NUM_TWO_PAIRS = 2
NUM_PAIRS = 1
FOUR_OF_A_KIND = 4
THREE_OF_A_KIND = 3
FLUSH = 4
TWO_PAIR = 3
PAIR = 2
HIGH_CARD = 1


class PokerHand:

    def __init__(self, card_list):
        """
        Constructs a PokerHand object with a given card list.

        :param card_list: List of cards that should be in the hand.
        """
        self.__card_list = card_list.copy()

    def get_hand(self):
        """
        Gets and returns hand.

        :return: The hand.
        """
        return self.__card_list

    def add_card(self, card):
        """
        Adds a card object to a list of cards.

        :param card: The given card object.
        :return: No return.
        """
        self.__card_list.append(card)

    def deal_hand(self, deck):
        """
        Creates a list of 5 cards to form a hand of cards.

        :param deck: A deck object.
        :return: No return.
        """
        for i in range(NUM_CARDS_IN_HAND):
            self.add_card(deck.deal_card())

    def __get_suits_in_hand(self):
        return [card.get_suit() for card in self.__card_list]

    def __get_first_suit_in_hand(self, suits_in_hand):
        return suits_in_hand[0]

    def __get_ranks_in_hand(self):
        return [card.get_rank() for card in self.__card_list]

    def __is_flush(self):
        is_flush = True
        suits_in_hand = self.__get_suits_in_hand()
        first_suit = self.__get_first_suit_in_hand(suits_in_hand)
        for _suit in range(1, len(suits_in_hand)):
            if suits_in_hand[_suit] != first_suit:
                is_flush = False
        return is_flush

    def __is_pair(self):
        is_pair = False
        ranks_in_hand = self.__get_ranks_in_hand()
        pairs = []
        for rank in ranks_in_hand:
            if rank not in pairs:
                if ranks_in_hand.count(rank) > 1:
                    pairs.append(rank)
        if len(pairs) == 1:
            is_pair = True

        return is_pair

    def __is_two_pair(self):
        is_two_pair = False
        pairs = []
        ranks_in_hand = self.__get_ranks_in_hand()
        for rank in ranks_in_hand:
            if rank not in pairs:
                if ranks_in_hand.count(rank) > 1:
                    pairs.append(rank)
                    if ranks_in_hand.count(rank) == FOUR_OF_A_KIND:
                        pairs.append(rank)

        if len(pairs) == 2:
            is_two_pair = True

        return is_two_pair

    def __hand_type(self):
        """
        Determines which kind of the four types (Flush, Pair, Two-Pair, or High Card) the card hand is.

        :return: A different value based on what type the hand is. (Flush>TwoPair>Pair>HighCard)
        """
        if self.__is_flush():
            return FLUSH
        elif self.__is_two_pair():
            return TWO_PAIR
        elif self.__is_pair():
            return PAIR
        else:
            return HIGH_CARD

    def __compare_ranks(self, ranks_1, ranks_2):
        """
        Compares two ranks' values.

        :param ranks_1: Given rank 1.
        :param ranks_2: Given rank 2.
        :return: 1 if rank 1 is greater than rank 2, 0 if they are equal, and -1 if rank 1 is less than rank 2
        """
        if ranks_1 > ranks_2:
            return HAND_1_WINS
        elif ranks_1 == ranks_2:
            return TIE
        else:
            return HAND_2_WINS

    def __compare_flush_or_high_card(self, hand_1_ranks, hand_2_ranks):
        """
        Compares two flush hands or two high-card hands and returns which hand wins.

        :param hand_1_ranks: Given list of ranks from hand.
        :param hand_2_ranks: Given list of ranks from hand.
        :return: 1 if hand 1 wins, -1 is hand 2 wins, and 0 if they tie
        """
        winning_hand = 0
        i = 0
        while winning_hand == 0 and i < NUM_CARDS_IN_HAND:
            winning_hand = self.__compare_ranks(hand_1_ranks[i], hand_2_ranks[i])
            i += 1

        return winning_hand

    def __get_pairs(self, hand_ranks):
        """
        Gets pairs from a list of ranks and creates a new list of pair ranks.

        :param hand_ranks: Given list of ranks in hand.
        :return: List of pair ranks.
        """
        pairs = []
        for rank in hand_ranks:
            if rank not in pairs:
                if hand_ranks.count(rank) > 1:
                    pairs.append(rank)
                    if hand_ranks.count(rank) == FOUR_OF_A_KIND:
                        pairs.append(rank)
        return pairs

    def __get_high_cards_in_pairs(self, hand_ranks):
        """
        Gets high cards from a list of pairs or two-pairs and creates a new list of high card ranks.

        :param hand_ranks: Given list of ranks in hand.
        :return: List of high cards (cards that are not pairs).
        """
        pairs = []
        high_card = []
        for rank in hand_ranks:
            if rank not in pairs:
                if hand_ranks.count(rank) > 1:
                    if hand_ranks.count(rank) == THREE_OF_A_KIND:
                        high_card.append(rank)
                    pairs.append(rank)
                else:
                    high_card.append(rank)

        return high_card

    def __compare_two_pair(self, hand_1_ranks, hand_2_ranks):
        """
        Compares two two-pair hands and returns which hand wins.

        :param hand_1_ranks: Given list of ranks from hand.
        :param hand_2_ranks: Given list of ranks from hand.
        :return: 1 if hand 1 wins, -1 is hand 2 wins, and 0 if they tie
        """
        pairs_hand_1 = self.__get_pairs(hand_1_ranks)
        high_card_hand_1 = self.__get_high_cards_in_pairs(hand_1_ranks)
        pairs_hand_2 = self.__get_pairs(hand_2_ranks)
        high_card_hand_2 = self.__get_high_cards_in_pairs(hand_2_ranks)

        winning_hand = 0
        i = 0
        while winning_hand == 0 and i < NUM_TWO_PAIRS:
            winning_hand = self.__compare_ranks(pairs_hand_1[i], pairs_hand_2[i])
            i += 1
        if winning_hand == 0:
            winning_hand = self.__compare_ranks(high_card_hand_1[0], high_card_hand_2[0])

        return winning_hand

    def __compare_pair(self, hand_1_ranks, hand_2_ranks):
        """
        Compares two pair hands and returns which hand wins.

        :param hand_1_ranks: Given list of ranks from hand.
        :param hand_2_ranks: Given list of ranks from hand.
        :return: 1 if hand 1 wins, -1 is hand 2 wins, and 0 if they tie
        """
        pairs_hand_1 = self.__get_pairs(hand_1_ranks)
        high_card_hand_1 = self.__get_high_cards_in_pairs(hand_1_ranks)
        pairs_hand_2 = self.__get_pairs(hand_2_ranks)
        high_card_hand_2 = self.__get_high_cards_in_pairs(hand_2_ranks)

        winning_hand = 0
        i = 0
        while winning_hand == 0 and i < NUM_PAIRS:
            winning_hand = self.__compare_ranks(pairs_hand_1[i], pairs_hand_2[i])
            i += 1
        if winning_hand == 0:
            while winning_hand == 0 and i < NUM_HIGH_CARDS_PAIR:
                winning_hand = self.__compare_ranks(high_card_hand_1[i], high_card_hand_2[i])
                i += 1

        return winning_hand

    def compare_to(self, other):
        """
        Determines how this hand compares to another hand, returns
        positive, negative, or zero depending on the comparison.

        :param self: the first hand to compare
        :param other: the second hand to compare
        :return: a negative number if self is worth LESS than other, zero
        if they are worth the SAME, and a positive number if self if worth
        MORE than other
        """
        hand_1_type = self.__hand_type()
        hand_2_type = other.__hand_type()

        if hand_1_type > hand_2_type:
            return HAND_1_WINS
        elif hand_1_type < hand_2_type:
            return HAND_2_WINS
        elif hand_1_type == hand_2_type:
            hand_1_ranks = self.__get_ranks_in_hand()
            hand_2_ranks = other.__get_ranks_in_hand()
            hand_1_ranks.sort(reverse=True)
            hand_2_ranks.sort(reverse=True)

            if hand_1_type == FLUSH:
                return self.__compare_flush_or_high_card(hand_1_ranks, hand_2_ranks)
            elif hand_1_type == TWO_PAIR:
                return self.__compare_two_pair(hand_1_ranks, hand_2_ranks)
            elif hand_1_type == PAIR:
                return self.__compare_pair(hand_1_ranks, hand_2_ranks)
            else:
                return self.__compare_flush_or_high_card(hand_1_ranks, hand_2_ranks)

    def __str__(self):
        player_hand = ''
        for card in self.__card_list:
            player_hand += card.__str__()
            player_hand += '\n'
        return player_hand


def __utest_compare_to_flush():
    u_test = test.create()

    hand_1_list = []
    hand_1 = PokerHand(hand_1_list)
    hand_2_list = []
    hand_2 = PokerHand(hand_2_list)
    hand_3_list = []
    hand_3 = PokerHand(hand_3_list)
    hand_4_list = []
    hand_4 = PokerHand(hand_4_list)

    hand_1.add_card(c.Card(3, "Spades"))
    hand_1.add_card(c.Card(14, "Spades"))
    hand_1.add_card(c.Card(8, "Spades"))
    hand_1.add_card(c.Card(5, "Spades"))
    hand_1.add_card(c.Card(10, "Spades"))

    hand_2.add_card(c.Card(2, "Hearts"))
    hand_2.add_card(c.Card(7, "Hearts"))
    hand_2.add_card(c.Card(14, "Hearts"))
    hand_2.add_card(c.Card(9, "Hearts"))
    hand_2.add_card(c.Card(13, "Hearts"))

    hand_3.add_card(c.Card(2, "Diamonds"))
    hand_3.add_card(c.Card(7, "Diamonds"))
    hand_3.add_card(c.Card(6, "Diamonds"))
    hand_3.add_card(c.Card(9, "Diamonds"))
    hand_3.add_card(c.Card(13, "Diamonds"))

    hand_4.add_card(c.Card(8, "Clubs"))
    hand_4.add_card(c.Card(5, "Clubs"))
    hand_4.add_card(c.Card(14, "Clubs"))
    hand_4.add_card(c.Card(3, "Clubs"))
    hand_4.add_card(c.Card(10, "Clubs"))

    winning_hand = hand_1.compare_to(hand_2)
    test.assert_equals(u_test, "Flush Test Hand 2 Wins", HAND_2_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_3)
    test.assert_equals(u_test, "Flush Test Hand 1 Wins", HAND_1_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_4)
    test.assert_equals(u_test, "Flush Test Hands Tie", TIE, winning_hand)

    test.print_summary(u_test)
    print()


def __u_test_compare_to_two_pair():
    u_test = test.create()

    hand_1_list = []
    hand_1 = PokerHand(hand_1_list)
    hand_2_list = []
    hand_2 = PokerHand(hand_2_list)
    hand_3_list = []
    hand_3 = PokerHand(hand_3_list)
    hand_4_list = []
    hand_4 = PokerHand(hand_4_list)
    hand_5_list = []
    hand_5 = PokerHand(hand_5_list)
    hand_6_list = []
    hand_6 = PokerHand(hand_6_list)

    hand_1.add_card(c.Card(3, "Spades"))
    hand_1.add_card(c.Card(3, "Diamonds"))
    hand_1.add_card(c.Card(8, "Spades"))
    hand_1.add_card(c.Card(8, "Clubs"))
    hand_1.add_card(c.Card(2, "Spades"))

    hand_2.add_card(c.Card(7, "Clubs"))
    hand_2.add_card(c.Card(7, "Hearts"))
    hand_2.add_card(c.Card(9, "Spades"))
    hand_2.add_card(c.Card(8, "Diamonds"))
    hand_2.add_card(c.Card(8, "Hearts"))

    hand_3.add_card(c.Card(6, "Spades"))
    hand_3.add_card(c.Card(6, "Hearts"))
    hand_3.add_card(c.Card(9, "Hearts"))
    hand_3.add_card(c.Card(4, "Diamonds"))
    hand_3.add_card(c.Card(4, "Hearts"))

    hand_4.add_card(c.Card(2, "Clubs"))
    hand_4.add_card(c.Card(3, "Clubs"))
    hand_4.add_card(c.Card(8, "Spades"))
    hand_4.add_card(c.Card(8, "Diamonds"))
    hand_4.add_card(c.Card(3, "Diamonds"))

    hand_5.add_card(c.Card(11, "Spades"))
    hand_5.add_card(c.Card(12, "Diamonds"))
    hand_5.add_card(c.Card(12, "Spades"))
    hand_5.add_card(c.Card(12, "Clubs"))
    hand_5.add_card(c.Card(12, "Spades"))

    hand_6.add_card(c.Card(11, "Spades"))
    hand_6.add_card(c.Card(11, "Diamonds"))
    hand_6.add_card(c.Card(12, "Spades"))
    hand_6.add_card(c.Card(12, "Clubs"))
    hand_6.add_card(c.Card(12, "Spades"))

    winning_hand = hand_1.compare_to(hand_2)
    test.assert_equals(u_test, "Two-Pair Test Hand 2 Wins", HAND_2_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_3)
    test.assert_equals(u_test, "Two-Pair Test Hand 1 Wins", HAND_1_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_4)
    test.assert_equals(u_test, "Two-Pair Test Hands Tie", TIE, winning_hand)

    winning_hand = hand_5.compare_to(hand_6)
    test.assert_equals(u_test, "Pair Test Hands 1 Wins", HAND_1_WINS, winning_hand)

    test.print_summary(u_test)
    print()


def __u_test_compare_to_pair():
    u_test = test.create()

    hand_1_list = []
    hand_1 = PokerHand(hand_1_list)
    hand_2_list = []
    hand_2 = PokerHand(hand_2_list)
    hand_3_list = []
    hand_3 = PokerHand(hand_3_list)
    hand_4_list = []
    hand_4 = PokerHand(hand_4_list)

    hand_1.add_card(c.Card(3, "Spades"))
    hand_1.add_card(c.Card(4, "Diamonds"))
    hand_1.add_card(c.Card(8, "Spades"))
    hand_1.add_card(c.Card(7, "Clubs"))
    hand_1.add_card(c.Card(8, "Spades"))

    hand_2.add_card(c.Card(2, "Clubs"))
    hand_2.add_card(c.Card(7, "Hearts"))
    hand_2.add_card(c.Card(11, "Spades"))
    hand_2.add_card(c.Card(8, "Diamonds"))
    hand_2.add_card(c.Card(11, "Hearts"))

    hand_3.add_card(c.Card(6, "Spades"))
    hand_3.add_card(c.Card(6, "Hearts"))
    hand_3.add_card(c.Card(9, "Hearts"))
    hand_3.add_card(c.Card(4, "Diamonds"))
    hand_3.add_card(c.Card(13, "Hearts"))

    hand_4.add_card(c.Card(7, "Clubs"))
    hand_4.add_card(c.Card(3, "Clubs"))
    hand_4.add_card(c.Card(8, "Spades"))
    hand_4.add_card(c.Card(8, "Diamonds"))
    hand_4.add_card(c.Card(4, "Diamonds"))

    winning_hand = hand_1.compare_to(hand_2)
    test.assert_equals(u_test, "Pair Test Hand 2 Wins", HAND_2_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_3)
    test.assert_equals(u_test, "Pair Test Hand 1 Wins", HAND_1_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_4)
    test.assert_equals(u_test, "Pair Test Hands Tie", TIE, winning_hand)

    test.print_summary(u_test)
    print()


def __u_test_compare_to_high_card():
    u_test = test.create()

    hand_1_list = []
    hand_1 = PokerHand(hand_1_list)
    hand_2_list = []
    hand_2 = PokerHand(hand_2_list)
    hand_3_list = []
    hand_3 = PokerHand(hand_3_list)
    hand_4_list = []
    hand_4 = PokerHand(hand_4_list)

    hand_1.add_card(c.Card(3, "Spades"))
    hand_1.add_card(c.Card(5, "Diamonds"))
    hand_1.add_card(c.Card(8, "Spades"))
    hand_1.add_card(c.Card(13, "Clubs"))
    hand_1.add_card(c.Card(10, "Spades"))

    hand_2.add_card(c.Card(2, "Clubs"))
    hand_2.add_card(c.Card(3, "Hearts"))
    hand_2.add_card(c.Card(9, "Spades"))
    hand_2.add_card(c.Card(14, "Diamonds"))
    hand_2.add_card(c.Card(6, "Hearts"))

    hand_3.add_card(c.Card(6, "Spades"))
    hand_3.add_card(c.Card(10, "Hearts"))
    hand_3.add_card(c.Card(9, "Hearts"))
    hand_3.add_card(c.Card(4, "Diamonds"))
    hand_3.add_card(c.Card(8, "Hearts"))

    hand_4.add_card(c.Card(13, "Clubs"))
    hand_4.add_card(c.Card(3, "Clubs"))
    hand_4.add_card(c.Card(8, "Spades"))
    hand_4.add_card(c.Card(5, "Diamonds"))
    hand_4.add_card(c.Card(10, "Diamonds"))

    winning_hand = hand_1.compare_to(hand_2)
    test.assert_equals(u_test, "High Card Test Hand 2 Wins", HAND_2_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_3)
    test.assert_equals(u_test, "High Card Test Hand 1 Wins", HAND_1_WINS, winning_hand)

    winning_hand = hand_1.compare_to(hand_4)
    test.assert_equals(u_test, "High Card Test Hands Tie", TIE, winning_hand)

    test.print_summary(u_test)

def __u_test_compare_types():
    u_test = test.create()

    hand_flush_list = []
    hand_flush = PokerHand(hand_flush_list)
    hand_two_pair_list = []
    hand_two_pair = PokerHand(hand_two_pair_list)
    hand_two_pair_list_2 = []
    hand_two_pair_2 = PokerHand(hand_two_pair_list_2)
    hand_two_pair_list_3 = []
    hand_two_pair_3 = PokerHand(hand_two_pair_list_3)
    hand_pair_list = []
    hand_pair = PokerHand(hand_pair_list)
    hand_pair_list_2 = []
    hand_pair_2 = PokerHand(hand_pair_list_2)
    hand_high_card_list = []
    hand_high_card = PokerHand(hand_high_card_list)

    hand_flush.add_card(c.Card(3, "Spades"))
    hand_flush.add_card(c.Card(14, "Spades"))
    hand_flush.add_card(c.Card(8, "Spades"))
    hand_flush.add_card(c.Card(5, "Spades"))
    hand_flush.add_card(c.Card(10, "Spades"))

    hand_two_pair.add_card(c.Card(3, "Spades"))
    hand_two_pair.add_card(c.Card(3, "Diamonds"))
    hand_two_pair.add_card(c.Card(8, "Spades"))
    hand_two_pair.add_card(c.Card(8, "Clubs"))
    hand_two_pair.add_card(c.Card(2, "Spades"))

    hand_two_pair_2.add_card(c.Card(9, "Spades"))
    hand_two_pair_2.add_card(c.Card(12, "Diamonds"))
    hand_two_pair_2.add_card(c.Card(12, "Spades"))
    hand_two_pair_2.add_card(c.Card(12, "Clubs"))
    hand_two_pair_2.add_card(c.Card(12, "Spades"))

    hand_two_pair_3.add_card(c.Card(2, "Spades"))
    hand_two_pair_3.add_card(c.Card(2, "Diamonds"))
    hand_two_pair_3.add_card(c.Card(12, "Spades"))
    hand_two_pair_3.add_card(c.Card(12, "Clubs"))
    hand_two_pair_3.add_card(c.Card(12, "Spades"))

    hand_pair.add_card(c.Card(3, "Spades"))
    hand_pair.add_card(c.Card(4, "Diamonds"))
    hand_pair.add_card(c.Card(8, "Spades"))
    hand_pair.add_card(c.Card(7, "Clubs"))
    hand_pair.add_card(c.Card(8, "Spades"))

    hand_pair_2.add_card(c.Card(3, "Spades"))
    hand_pair_2.add_card(c.Card(4, "Diamonds"))
    hand_pair_2.add_card(c.Card(7, "Spades"))
    hand_pair_2.add_card(c.Card(7, "Clubs"))
    hand_pair_2.add_card(c.Card(7, "Spades"))

    hand_high_card.add_card(c.Card(3, "Spades"))
    hand_high_card.add_card(c.Card(5, "Diamonds"))
    hand_high_card.add_card(c.Card(8, "Spades"))
    hand_high_card.add_card(c.Card(13, "Clubs"))
    hand_high_card.add_card(c.Card(10, "Spades"))

    winning_hand = hand_flush.compare_to(hand_two_pair)
    test.assert_equals(u_test, "Flush vs Two Pair Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_flush.compare_to(hand_two_pair_2)
    test.assert_equals(u_test, "Flush vs Two Pair 2 Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_flush.compare_to(hand_two_pair_3)
    test.assert_equals(u_test, "Flush vs Two Pair 2 Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_flush.compare_to(hand_pair)
    test.assert_equals(u_test, "Flush vs Pair Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_flush.compare_to(hand_pair_2)
    test.assert_equals(u_test, "Flush vs Pair 2 Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_flush.compare_to(hand_high_card)
    test.assert_equals(u_test, "Flush vs High Card Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair.compare_to(hand_two_pair_2)
    test.assert_equals(u_test, "Two Pair vs Two Pair 2 Test (Hand 2 Wins[-1])", HAND_2_WINS, winning_hand)

    winning_hand = hand_two_pair.compare_to(hand_two_pair_3)
    test.assert_equals(u_test, "Flush vs Two Pair 2 Test (Hand 2 Wins [-1])", HAND_2_WINS, winning_hand)

    winning_hand = hand_two_pair.compare_to(hand_pair)
    test.assert_equals(u_test, "Two Pair vs Pair Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair.compare_to(hand_pair_2)
    test.assert_equals(u_test, "Two Pair vs Pair 2 Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair.compare_to(hand_high_card)
    test.assert_equals(u_test, "Two Pair vs High Card Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_2.compare_to(hand_two_pair_3)
    test.assert_equals(u_test, "Two Pair 2 vs Pair Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_2.compare_to(hand_pair)
    test.assert_equals(u_test, "Two Pair 2 vs Pair Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_2.compare_to(hand_pair_2)
    test.assert_equals(u_test, "Two Pair 2 vs Pair 2 Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_2.compare_to(hand_high_card)
    test.assert_equals(u_test, "Two Pair 2 vs High Card Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_3.compare_to(hand_pair)
    test.assert_equals(u_test, "Flush vs Two Pair 2 Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_3.compare_to(hand_pair_2)
    test.assert_equals(u_test, "Flush vs Two Pair 2 Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_two_pair_3.compare_to(hand_high_card)
    test.assert_equals(u_test, "Flush vs Two Pair 2 Test (Hand 1 Wins [1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_pair.compare_to(hand_pair_2)
    test.assert_equals(u_test, "Pair vs Pair 2 Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_pair.compare_to(hand_high_card)
    test.assert_equals(u_test, "Pair vs High Card Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    winning_hand = hand_pair_2.compare_to(hand_high_card)
    test.assert_equals(u_test, "Pair 2 vs High Card Test (Hand 1 Wins[1])", HAND_1_WINS, winning_hand)

    test.print_summary(u_test)

if __name__ == '__main__':
    __utest_compare_to_flush()
    __u_test_compare_to_two_pair()
    __u_test_compare_to_pair()
    __u_test_compare_to_high_card()
    __u_test_compare_types()
