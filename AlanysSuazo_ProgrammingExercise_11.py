# Alanys Suazo
# Assignment: Programming Exercise 11

# The purpose of this assignment is to create a game program using the deck object. The program should deal
#    a poker hand of 5 cards, after which it wil prompt the user to enter a series of numbersthat selects cards
#    from the hands to be replaced, and print the results of the new hand.

#importing the package needed for the program to work
import random

# following the textbook as reference, using a class to create the game functions
class Deck:
    # using a code in the textbook as reference to making the deck with pictograms
    def __init__(self, n_decks = 1):
        self.card_list = [num + suit
                          for suit in '\u2665\u2666\u2663\u2660'
                          for num in 'A23456789TJQK'
                          for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    #function to dealing cards
    def deal(self):
        # if the deck is empty, recyle the remaining cards
        if len(self.card_list) < 1:
            if not self.discards_list:
                raise ValueError('No cards left to deal')
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    #moves all the cards in play to the discard pile
    def new_hand(self):
        self.discards_list.extend(self.cards_in_play_list)
        self.cards_in_play_list.clear()


    def deal_poker_hand(self):
        return [self.deal() for deck in range(5)]

    def draw_phase(self, hand):
        print("\nYour current hand:")
        for i, card in enumerate(hand, start=1):
            print(f"{i}: {card}")

        replace = input("Enter card numbers to replace (e.g., 1,3,5), or press Enter to keep all: ")
        if replace.strip() == "":
            return hand

        indices = [int(x) for x in replace.split(",")]

        for i in indices:
            if 1 <= i <= 5:
                hand[i - 1] = self.deal()

        return hand


def main():
    deck = Deck(1)
    hand = deal_poker_hand(deck)

    print("Initial hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")

    hand = deck.draw_phase(hand)

    print("\nFinal hand after draw:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")


if __name__ == "-__main__":
    main()