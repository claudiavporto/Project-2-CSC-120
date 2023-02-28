import poker_hand as h
import deck as d

NUM_CARDS_IN_HAND = 5


def main():
    game_deck = d.Deck()

    correct_answer = True
    total_score = 0
    hand_1_list = []
    hand_2_list = []

    while not game_deck.less_than_5_cards() and correct_answer:
        # draw hand 1
        print('Hand 1:')
        hand_1 = h.PokerHand(hand_1_list)
        hand_1.deal_hand(game_deck)
        print(hand_1)

        # draw hand 2
        print('Hand 2:')
        hand_2 = h.PokerHand(hand_2_list)
        hand_2.deal_hand(game_deck)
        print(hand_2)

        # compare_to
        actual_result = hand_1.compare_to(hand_2)

        user_guess = input("Which hand is worth more? Are they equal?\nEnter 1 for Hand 1,"
                           " -1 for Hand 2, or 0 for a Tie\n")

        if actual_result != int(user_guess):
            correct_answer = False
            print(f'Sorry! You lost!\nThe correct answer was {actual_result}.')
        else:
            total_score += 1
            print('Nice! You got it right!\n')

    print(f'Final score: {total_score}')


if __name__ == '__main__':
    main()
